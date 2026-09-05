import json
import shutil
import tempfile
import unittest
from pathlib import Path

from pipeline.render_guard import (
    GuardError,
    active_episode_id,
    authorize,
    compile_prompt,
    validate_repository,
    validate_episode_plan,
)

REPO = Path(__file__).resolve().parents[1]


class RenderGuardTests(unittest.TestCase):
    def _active(self):
        return active_episode_id(REPO)

    def _active_plan_manifest(self):
        eid = self._active()
        plan = json.loads((REPO / "episodes" / eid / "EPISODE_PLAN.json").read_text(encoding="utf-8"))
        manifest = json.loads((REPO / "episodes" / eid / "RENDER_MANIFEST.json").read_text(encoding="utf-8"))
        return eid, plan, manifest

    def _supply_all_required(self):
        _, _, manifest = self._active_plan_manifest()
        return [
            {
                "requirement_id": r["requirement_id"],
                "source_id": r["source_id"],
                "media_type": r["media_type"],
                "actual_hash": r.get("expected_hash"),
            }
            for r in manifest["media_requirements"]
            if r.get("required") is True and r.get("conditioning") == "MUST_SUPPLY_MEDIA"
        ]

    def test_active_episode_validates(self):
        eid = self._active()
        plan, _ = validate_repository(REPO, eid)
        self.assertEqual(plan["episode_id"], eid)

    def test_non_active_episode_fails(self):
        active = self._active()
        candidates = sorted(
            p.parent.name
            for p in (REPO / "episodes").glob("E*/EPISODE_PLAN.json")
            if p.parent.name != active
            and (p.parent / "RENDER_MANIFEST.json").is_file()
            and json.loads(p.read_text(encoding="utf-8")).get("schema_version") == "1.0"
        )
        if not candidates:
            self.skipTest("no non-active canonical episode")
        with self.assertRaises(GuardError):
            validate_repository(REPO, candidates[-1])

    def test_compiled_prompt_contains_generic_media_requirements(self):
        eid, plan, manifest = self._active_plan_manifest()
        prompt = compile_prompt(REPO, eid, 1)
        self.assertIn(plan["slides"][0]["slide_id"], prompt)
        self.assertIn("REQUIRED MEDIA INPUTS:", prompt)
        for req in manifest["media_requirements"]:
            if req.get("required") is True:
                self.assertIn(req["requirement_id"], prompt)
                self.assertIn(req["source_id"], prompt)

    def test_blocks_renderer_without_explicit_media_support(self):
        eid, _, _ = self._active_plan_manifest()
        with self.assertRaises(GuardError):
            authorize(REPO, eid, 1, "CONVERSATION_INFERRED", "NOT_RUN", False, ["image"], [])

    def test_blocks_missing_required_media(self):
        eid, _, _ = self._active_plan_manifest()
        with self.assertRaises(GuardError):
            authorize(REPO, eid, 1, "CONVERSATION_INFERRED", "NOT_RUN", True, ["image"], [])

    def test_blocks_wrong_media_type_capability(self):
        eid, _, _ = self._active_plan_manifest()
        with self.assertRaises(GuardError):
            authorize(REPO, eid, 1, "CONVERSATION_INFERRED", "NOT_RUN", True, ["audio"], self._supply_all_required())

    def test_authorizes_when_generic_media_requirements_are_satisfied(self):
        eid, _, _ = self._active_plan_manifest()
        self.assertEqual(
            authorize(
                REPO, eid, 1, "CONVERSATION_INFERRED", "NOT_RUN",
                True, ["image"], self._supply_all_required()
            ),
            "AUTHORIZED_SEQUENTIAL_SINGLE_FRAME",
        )

    def test_conversation_inferred_cannot_skip_frame_qc(self):
        eid, plan, _ = self._active_plan_manifest()
        if plan["format"]["slide_count"] < 2:
            self.skipTest("active episode has only one slide")
        supply = self._supply_all_required()
        with self.assertRaises(GuardError):
            authorize(REPO, eid, 2, "CONVERSATION_INFERRED", "NOT_RUN", True, ["image"], supply)
        self.assertEqual(
            authorize(REPO, eid, 2, "CONVERSATION_INFERRED", "PASS", True, ["image"], supply),
            "AUTHORIZED_SEQUENTIAL_SINGLE_FRAME",
        )

    def test_multi_panel_or_combined_delivery_is_rejected(self):
        for field, bad in [("panels_per_image", 4), ("panels_per_image", None),
                           ("delivery_mode", "CONTACT_SHEET")]:
            with self.subTest(field=field, value=bad):
                _, plan, _ = self._active_plan_manifest()
                plan["format"][field] = bad
                with self.assertRaises(GuardError):
                    validate_episode_plan(plan)

    def test_single_panel_compiler_isolates_requested_scene(self):
        eid, plan, _ = self._active_plan_manifest()
        prompt = compile_prompt(REPO, eid, 1)
        self.assertIn("Exactly ONE panel in ONE image", prompt)
        self.assertIn("Reference sheets are input references only", prompt)
        if len(plan["slides"]) > 1:
            self.assertNotIn(plan["slides"][1]["slide_id"], prompt)
            self.assertNotIn(plan["slides"][1]["action"], prompt)

    def test_duplicate_active_episode_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            eid = self._active()
            line = f"Active episode: episodes/{eid}/README.md\n"
            (root / "CURRENT_STATE.md").write_text(line + line)
            with self.assertRaises(GuardError):
                active_episode_id(root)

    def test_changed_reference_bytes_are_rejected(self):
        eid, _, manifest = self._active_plan_manifest()
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "repo"
            shutil.copytree(REPO, root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            (root / manifest["style_refs"][0]).write_bytes(b"not the approved image")
            with self.assertRaisesRegex(GuardError, "local media SHA-256 mismatch"):
                validate_repository(root, eid)

    def test_required_local_media_cannot_drop_integrity_hash(self):
        eid, _, manifest = self._active_plan_manifest()
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "repo"
            shutil.copytree(REPO, root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            manifest["media_requirements"][0]["expected_hash"] = None
            (root / "episodes" / eid / "RENDER_MANIFEST.json").write_text(json.dumps(manifest))
            with self.assertRaisesRegex(GuardError, "needs a SHA-256"):
                validate_repository(root, eid)

    def test_stale_manifest_fails_closed(self):
        active = self._active()
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "repo"
            shutil.copytree(REPO, root, dirs_exist_ok=True)
            plan_path = root / "episodes" / active / "EPISODE_PLAN.json"
            plan_path.write_text(plan_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            with self.assertRaises(GuardError):
                validate_repository(root, active)


if __name__ == "__main__":
    unittest.main()
