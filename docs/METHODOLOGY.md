# Evidence, calibration and limits

## Evidence tiers

1. **Directly inspected:** curated export PNGs (including measured color values), source identifier inventory and capture logs provided by the author.
2. **Reported from original application's audit:** code-path references and chart dispatcher names preserved in the earlier skill.
3. **Suggested procedure:** render-ready gate, checking semantics, tests and exported-file integrity; these are design guidance and not proof of implementation in the source app.

The PNG archive used for review contained 56 PNGs: 51 named ordinary exports, two intentionally labeled screenshot fallbacks and three page screenshots. The author replaced 12 previously identical blank exports with content-bearing PNGs after waiting for the true chart render. Two historical CORS-related failures remained unrelated to that timing race. **The full archive is not included**, both to keep the skill lean and to avoid leaking unrelated browser/authentication traces.

The seven image references in this repo are representative, **not** a statistically sampled benchmark and **not** guaranteed to contain perfect spacing or analytics. In particular, a max-bar annotation may be clipped in a reference; agents should fix a visible defect, not reproduce it.

The reference images document the light PNG report surface. They cannot establish the portal's dark interactive theme tokens or exact original CSS. `design-tokens.json` records measured colors with explicit provenance; values are visual reference points only.

## Evaluation protocol (not yet run)

Evaluate a baseline agent versus the same agent plus the skill on identical financial datasets, chart engine, fonts, viewports and runtime limits. Blind reviewers should rate: numeric/date correctness (hard gate), chart choice, accessibility/legibility, export completeness and faithful but sensible visual styling. Record runtime and token usage as secondary metrics, report failures and avoid cherry-picking. The offline `tests/evals.json` defines scenarios, **not completed benchmark runs**.
