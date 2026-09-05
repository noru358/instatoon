import shutil
import tempfile
import unittest
from pathlib import Path
from pipeline.render_guard import GuardError, authorize, compile_prompt, validate_repository

REPO = Path(__file__).resolve().parents[1]

class RenderGuardTests(unittest.TestCase):
    def test_active_e004_validates(self):
        plan, _ = validate_repository(REPO, "E004")
        self.assertEqual(plan["episode_id"], "E004")

    def test_wrong_active_episode_fails(self):
        with self.assertRaises(GuardError):
            validate_repository(REPO, "E003")

    def test_compiled_prompt_is_bound_to_e004(self):
        prompt = compile_prompt(REPO, "E004", 3)
        for token in ("E004_S03", "17", "21", "Taemin", "No readable captions"):
            self.assertIn(token, prompt)
        lowered = prompt.lower()
        for bad in ("fluffy white dog", "git status", "productive day"):
            self.assertNotIn(bad, lowered)

    def test_conversation_inferred_cannot_skip_frame_qc(self):
        with self.assertRaises(GuardError):
            authorize(REPO, "E004", 2, "CONVERSATION_INFERRED", "NOT_RUN")
        self.assertEqual(
            authorize(REPO, "E004", 2, "CONVERSATION_INFERRED", "PASS"),
            "AUTHORIZED_SEQUENTIAL_SINGLE_FRAME"
        )

    def test_stale_manifest_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "repo"
            shutil.copytree(REPO, root, dirs_exist_ok=True)
            plan_path = root / "episodes" / "E004" / "EPISODE_PLAN.json"
            plan_path.write_text(plan_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            with self.assertRaises(GuardError):
                validate_repository(root, "E004")

if __name__ == "__main__":
    unittest.main()
