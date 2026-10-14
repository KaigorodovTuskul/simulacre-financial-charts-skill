#!/usr/bin/env python3
"""Audit whitelisted PNG metadata in a Playwright MCP ZIP without extracting logs.

Checks identifier coverage, PNG signature/dimensions, exact duplicates and suspicious
small files. It deliberately does NOT claim image content or data are correct.
"""
import argparse
import collections
import hashlib
import json
import struct
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "skills/simulacre-financial-charts/references/indicator-catalog.json"


def inspect(archive):
    ids = {x["id"] for x in json.loads(CATALOG.read_text(encoding="utf-8"))["indicators"]}
    expected = {i.replace("_", "-") + ".png" for i in ids}
    fallback_pairs = {
        "global-market-heatmap-fallback.png": "global-market-heatmap.png",
        "russia-rgbi-ofz-constituents-fallback.png": "russia-rgbi-ofz-constituents.png",
    }
    records = []
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():
            name = Path(info.filename).name
            if not name.lower().endswith(".png"):
                continue
            is_page = name.startswith("page-")
            is_fallback = name in fallback_pairs
            if not (is_page or is_fallback or name in expected):
                category = "UNKNOWN_PNG"
            else:
                category = "PAGE" if is_page else "FALLBACK_SCREENSHOT" if is_fallback else "CHART_PNG"
            b = z.read(info)
            valid = len(b) >= 24 and b[:8] == b"\x89PNG\r\n\x1a\n"
            w, h = struct.unpack(">II", b[16:24]) if valid else (0, 0)
            records.append({"name": name, "category": category, "size": len(b), "width": w, "height": h, "sha256": hashlib.sha256(b).hexdigest(), "valid_png_header": valid})

    ordinary = [x for x in records if x["category"] == "CHART_PNG"]
    known = {x["name"] for x in ordinary}
    accounted = known | {fallback_pairs[x["name"]] for x in records if x["category"] == "FALLBACK_SCREENSHOT"}
    duplicates = [sorted([x["name"] for x in group]) for group in (
        g for g in ( [x for x in ordinary if x["sha256"] == digest] for digest in {y["sha256"] for y in ordinary}) if len(g) > 1
    )]
    problems = []
    if len(ordinary) != 51:
        problems.append(f"Expected 51 ordinary indicator PNGs; found {len(ordinary)}")
    if len([x for x in records if x["category"] == "FALLBACK_SCREENSHOT"]) != 2:
        problems.append("Expected two fallback screenshot PNGs")
    if len(accounted) != 53 or expected != accounted:
        problems.append("Indicator coverage mismatch: " + ", ".join(sorted(expected - accounted)))
    if duplicates:
        problems.append(f"Duplicated ordinary PNG content: {duplicates}")
    if any(not x["valid_png_header"] or x["width"] < 500 or x["height"] < 400 for x in ordinary):
        problems.append("Invalid PNG header or unexpected image dimensions")
    # Advisory only: tiny size does not necessarily imply a blank plot.
    warnings = [f"Possibly empty/small image: {x['name']} ({x['size']} bytes)" for x in ordinary if x["size"] < 25000]
    return {"archive": str(archive), "total_png": len(records), "chart_png": len(ordinary), "fallback_screenshots": len([x for x in records if x["category"] == "FALLBACK_SCREENSHOT"]), "page_screenshots": len([x for x in records if x["category"] == "PAGE"]), "unique_chart_hashes": len({x["sha256"] for x in ordinary}), "errors": problems, "warnings": warnings, "limitation": "Metadata-only smoke audit; unique PNG hashes do not prove chart-content completeness or data correctness."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path, help="Local .playwright-mcp ZIP path; ZIP is not uploaded or extracted")
    args = parser.parse_args()
    result = inspect(args.archive)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
