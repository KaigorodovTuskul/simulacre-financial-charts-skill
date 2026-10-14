# Apply this proposed v0.2.0 upgrade

The original GitHub `master` was not modified by this delivery. The current connection refused branch creation with `403 Resource not accessible by integration`.

## Recommended: overlay onto the existing repository

1. Clone or open your existing repository (the examples assume Git is installed).
2. Create a reviewable feature branch:

```bash
git switch -c feat/skill-v0.2-render-qa
```

3. Unzip **`simulacre_financial_charts_v0.2_overlay.zip`** into the repository root, overwriting files with the same names. This package has **no replacement PNGs**: all seven original GitHub image blobs were preserved byte-for-byte in the complete deliverable.
4. Check the result:

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

5. Optionally validate your local Playwright capture archive **without committing it**:

```bash
python scripts/audit_playwright_archive.py "/path/to/.playwright-mcp(1).zip"
```

6. Review, commit and publish:

```bash
git diff --check
git status
git add README.md LICENSE CHANGELOG.md CONTRIBUTING.md SECURITY.md AGENTS.md .gitignore docs/ examples/ scripts/ tests/ .github/ skills/simulacre-financial-charts/SKILL.md skills/simulacre-financial-charts/agents/openai.yaml skills/simulacre-financial-charts/references/
git commit -m "feat: improve financial chart semantics, export QA and skill packaging"
git push -u origin feat/skill-v0.2-render-qa
```

Open a pull request against `master` and review its file list before merging. Confirm that no browser archive, auth log or unreviewed PNG was committed. The complete ZIP is also available for inspecting the proposed full tree offline; **do not merge it over the original Git history**.
