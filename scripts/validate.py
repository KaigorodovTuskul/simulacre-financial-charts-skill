#!/usr/bin/env python3
"""Dependency-free Agent Skills structure and curated-reference preflight.

No browser execution and no claim of rendered-chart semantic correctness.
"""
import hashlib
import json
import re
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "simulacre-financial-charts"
REF = SKILL / "references"
ASSET = SKILL / "assets" / "reference-charts"


def check_markdown_links():
    errors = []
    pattern = re.compile(r"\]\(([^)]+)\)")
    html_pattern = re.compile(r'''(?:href|src)="([^"]+)"''')
    for f in ROOT.rglob("*.md"):
        contents = f.read_text(encoding="utf-8")
        local = pattern.findall(contents) + html_pattern.findall(contents)
        for raw in local:
            dest = raw.split("#", 1)[0]
            if not dest or dest.startswith(("https://", "http://", "mailto:", "data:")):
                continue
            # This repository does not use remote-relative HTML URLs.
            if dest.startswith("/"):
                errors.append(f"Absolute local link in {f.relative_to(ROOT)}: {dest}")
                continue
            path = (f.parent / dest).resolve()
            if not path.is_relative_to(ROOT.resolve()) or not path.exists():
                errors.append(f"Invalid link in {f.relative_to(ROOT)}: {raw}")
    return errors


def check_frontmatter():
    errors = []
    contents = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    parts = contents.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        return ["SKILL.md must begin with YAML frontmatter"]
    meta = parts[1]
    n = re.search(r"(?m)^name:\s*(.+)$", meta)
    d = re.search(r"(?m)^description:\s*(.+)$", meta)
    if not n or n.group(1).strip() != SKILL.name:
        errors.append("Skill name must match its directory")
    elif not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", n.group(1).strip()):
        errors.append("Skill name contains invalid characters")
    if not d or not 1 <= len(d.group(1).strip().strip('"')) <= 1024:
        errors.append("Missing or too-long description")
    if len(contents.splitlines()) > 500:
        errors.append("SKILL.md exceeds suggested 500-line limit")
    return errors


def check_catalog():
    errors = []
    data = json.loads((REF / "indicator-catalog.json").read_text(encoding="utf-8"))
    indicators = data["indicators"]
    ids = [x["id"] for x in indicators]
    if len(ids) != 53 or len(set(ids)) != 53:
        errors.append("Catalog must have 53 distinct indicator IDs")
    if ids != sorted(ids):
        errors.append("Catalog indicator IDs must be sorted")
    if len([x for x in indicators if x["source_template_family"] == "market_heatmap"]) != 1:
        errors.append("Expected one heatmap source family")
    if not any(x["id"] == "russia_weekly_cpi" and x["recommended_primary_pattern"] == "seasonal_overlay" for x in indicators):
        errors.append("Seasonal CPI active-view override missing")
    if not any(x["id"] == "russia_ofz_yield_curve_monitor" and x["recommended_primary_pattern"] == "yield_scatter" for x in indicators):
        errors.append("OFZ active-view override missing")
    return errors


def check_assets(asset_dir=ASSET, manifest_path=None):
    errors = []
    manifest_path = manifest_path or REF / "reference-manifest.json"
    data = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    items = data["images"]
    if len(items) != 7 or data.get("image_count") != 7:
        errors.append("Reference manifest must contain seven curated images")
    if len({x["file"] for x in items}) != len(items):
        errors.append("Duplicate image name in reference manifest")
    if len([x for x in items if x["status"] == "FALLBACK_SCREENSHOT"]) != 2:
        errors.append("Expected exactly two labeled fallback screenshots")
    paths = set()
    for item in items:
        filename = item["file"]
        if Path(filename).name != filename or not filename.endswith(".png"):
            errors.append(f"Unexpected asset path: {filename}")
            continue
        p = asset_dir / filename
        paths.add(filename)
        if not p.is_file():
            errors.append(f"Missing PNG reference: {filename}")
            continue
        raw = p.read_bytes()
        if hashlib.sha256(raw).hexdigest() != item["sha256"]:
            errors.append(f"PNG SHA-256 mismatch: {filename}")
        if len(raw) < 24 or raw[:8] != b"\x89PNG\r\n\x1a\n":
            errors.append(f"Invalid PNG signature: {filename}")
            continue
        w, h = struct.unpack(">II", raw[16:24])
        if (w, h) != (item["width"], item["height"]):
            errors.append(f"PNG dimensions mismatch: {filename}")
        if w < 500 or h < 400:
            errors.append(f"Unexpectedly small image: {filename}")
    if {p.name for p in asset_dir.glob("*.png")} != paths:
        errors.append("Curated asset folder and reference manifest differ")
    return errors


def check_evals():
    errors = []
    e = json.loads((ROOT / "tests" / "evals.json").read_text(encoding="utf-8"))
    cases = e["scenarios"]
    ids = [c["id"] for c in cases]
    if len(ids) != len(set(ids)) or len(cases) < 6:
        errors.append("Evaluation scenarios missing or duplicated")
    for c in cases:
        if not c.get("prompt") or not isinstance(c.get("must"), list) or not c["must"]:
            errors.append(f"Incomplete evaluation scenario: {c.get('id')}")
    return errors


def validate():
    errors = []
    for path in (ROOT / "LICENSE", ROOT / "README.md", ROOT / "CHANGELOG.md", SKILL / "agents" / "openai.yaml"):
        if not path.is_file():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")
    errors.extend(check_frontmatter())
    errors.extend(check_markdown_links())
    errors.extend(check_catalog())
    errors.extend(check_assets())
    errors.extend(check_evals())
    for f in ROOT.rglob("*"):
        if f.is_file() and (".playwright-mcp" in f.name or f.suffix.lower() in {".har"}):
            errors.append(f"Browser trace/secret risk: {f.relative_to(ROOT)}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        for issue in problems:
            print("FAIL:", issue, file=sys.stderr)
        sys.exit(1)
    print("PASS: skill frontmatter, 53 IDs, seven pinned PNGs, Markdown links and eval scenarios")
