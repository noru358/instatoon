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
)

REPO = Path(__file__).resolve().parents[1]


class RenderGuardTests(unittest.TestCase):
    def _active(self):
        return active_episode_id(REPO)

    def _active_plan(self):
        eid = self._active()
        return eid, json.loads(
            (REPO / "episodes" / eid / "EPISODE_PLAN.json").read_text(encoding="utf-8")
        )

    def _required_refs(self):
        _, plan = self._active_plan()
        return plan["style"]["required_refs"]

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
            self.skipTest("no non-active canonical episode with a render manifest")
        with self.assertRaises(GuardError):
            validate_repository(REPO, candidates[-1])

    def test_compiled_prompt_is_bound_to_active_plan(self):
        eid, plan = self._active_plan()
        slide = plan["slides"][0]
        prompt = compile_prompt(REPO, eid, 1)

        self.assertIn(slide["slide_id"], prompt)
        self.assertIn("RASTER_TEXT: NONE", prompt)
        self.assertIn("REFERENCE_CONDITIONING_REQUIRED:", prompt)
        self.assertIn(slide["story_clarity"], prompt)
        for entity in slide["required_entities"][:2]:
            self.assertIn(entity, prompt)

    def test_binary_required_blocks_authority_only(self):
        eid, _ = self._active_plan()
        with self.assertRaises(GuardError):
            authorize(
                REPO, eid, 1, "CONVERSATION_INFERRED", "NOT_RUN",
                "AUTHORITY_INFORMED_NON_BINARY_CONDITIONED", []
            )

    def test_binary_required_blocks_missing_media_evidence(self):
        eid, _ = self._active_plan()
        with self.assertRaises(GuardError):
            authorize(
                REPO, eid, 1, "CONVERSATION_INFERRED", "NOT_RUN",
                "BINARY_CONDITIONED", []
            )

    def test_binary_required_authorizes_when_all_refs_supplied(self):
        eid, _ = self._active_plan()
        self.assertEqual(
            authorize(
                REPO, eid, 1, "CONVERSATION_INFERRED", "NOT_RUN",
                "BINARY_CONDITIONED", self._required_refs()
            ),
            "AUTHORIZED_SEQUENTIAL_SINGLE_FRAME",
        )

    def test_conversation_inferred_cannot_skip_frame_qc(self):
        eid, plan = self._active_plan()
        if plan["format"]["slide_count"] < 2:
            self.skipTest("active episode has only one slide")
        refs = self._required_refs()
        with self.assertRaises(GuardError):
            authorize(
                REPO, eid, 2, "CONVERSATION_INFERRED", "NOT_RUN",
                "BINARY_CONDITIONED", refs
            )
        self.assertEqual(
            authorize(
                REPO, eid, 2, "CONVERSATION_INFERRED", "PASS",
                "BINARY_CONDITIONED", refs
            ),
            "AUTHORIZED_SEQUENTIAL_SINGLE_FRAME",
        )

    def test_stale_manifest_fails_closed(self):
        active = self._active()
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "repo"
            shutil.copytree(REPO, root, dirs_exist_ok=True)
            plan_path = root / "episodes" / active / "EPISODE_PLAN.json"
            plan_path.write_text(
                plan_path.read_text(encoding="utf-8") + "\n",
                encoding="utf-8",
            )
            with self.assertRaises(GuardError):
                validate_repository(root, active)


if __name__ == "__main__":
    unittest.main()
