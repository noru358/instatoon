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
        )
        if not candidates:
            self.skipTest("no non-active episode with a render manifest")
        with self.assertRaises(GuardError):
            validate_repository(REPO, candidates[-1])

    def test_compiled_prompt_is_bound_to_active_plan(self):
        eid, plan = self._active_plan()
        slide = plan["slides"][0]
        prompt = compile_prompt(REPO, eid, 1)

        self.assertIn(slide["slide_id"], prompt)
        self.assertIn("RASTER_TEXT: NONE", prompt)
        self.assertIn(slide["story_clarity"], prompt)
        for entity in slide["required_entities"][:2]:
            self.assertIn(entity, prompt)

        lowered = prompt.lower()
        for bad in ("fluffy white dog", "git status", "productive day"):
            self.assertNotIn(bad, lowered)

    def test_conversation_inferred_cannot_skip_frame_qc(self):
        eid, plan = self._active_plan()
        if plan["format"]["slide_count"] < 2:
            self.skipTest("active episode has only one slide")
        with self.assertRaises(GuardError):
            authorize(REPO, eid, 2, "CONVERSATION_INFERRED", "NOT_RUN")
        self.assertEqual(
            authorize(REPO, eid, 2, "CONVERSATION_INFERRED", "PASS"),
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
