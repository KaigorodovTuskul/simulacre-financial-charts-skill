"""Offline tests for static structure and documented source/integrity gates."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate as v  # noqa: E402


class SkillRepoIntegrity(unittest.TestCase):
    def test_repository_preflight(self):
        self.assertEqual(v.validate(), [])

    def test_53_unique_indicators(self):
        data = json.loads((v.REF / "indicator-catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(len(data["indicators"]), 53)
        self.assertEqual(len({i["id"] for i in data["indicators"]}), 53)
        counts = {}
        for item in data["indicators"]:
            counts[item["source_template_family"]] = counts.get(item["source_template_family"], 0) + 1
        self.assertEqual(counts, {"line": 25, "bar": 18, "delta_bar": 5, "stacked_bar": 4, "market_heatmap": 1})

    def test_fallbacks_not_called_exports(self):
        data = json.loads((v.REF / "reference-manifest.json").read_text(encoding="utf-8"))
        fallback = {x["file"] for x in data["images"] if x["status"] == "FALLBACK_SCREENSHOT"}
        self.assertEqual(fallback, {"global-market-heatmap-fallback.png", "russia-rgbi-ofz-constituents-fallback.png"})

    def test_mutated_png_fails_integrity(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            for ref in v.ASSET.glob("*.png"):
                (p / ref.name).write_bytes(ref.read_bytes())
            file = p / "global-dxy.png"
            file.write_bytes(file.read_bytes() + b"modified")
            errors = v.check_assets(asset_dir=p)
            self.assertTrue(any("SHA-256 mismatch" in s for s in errors), errors)

    def test_semantics_and_render_ready_gates_present(self):
        skill = (v.SKILL / "SKILL.md").read_text(encoding="utf-8")
        export = (v.REF / "capture-and-export.md").read_text(encoding="utf-8")
        self.assertIn("financial-semantics.md", skill)
        self.assertIn("render-ready gate", export.lower())
        self.assertIn("FALLBACK_SCREENSHOT", export)
        self.assertIn("SecurityError", export)


if __name__ == "__main__":
    unittest.main()
