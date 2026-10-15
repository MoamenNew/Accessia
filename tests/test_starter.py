import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class StarterTests(unittest.TestCase):
    def test_guides_exist(self):
        self.assertTrue((ROOT / 'AGENTS.md').is_file())
        self.assertTrue((ROOT / 'START_HERE.md').is_file())

    def test_approval_gate_written(self):
        txt = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
        self.assertIn('أوافق على الخطة', txt)
        self.assertIn('explicit', txt.lower())

    def test_prompts_present(self):
        self.assertEqual(len(list((ROOT / 'prompts').glob('*.txt'))), 6)

if __name__ == '__main__':
    unittest.main()
