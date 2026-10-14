---
name: simulacre-financial-charts
description: "Design, implement, review, or export decision-grade financial and macroeconomic charts. Use for market-data visualizations including time-series lines, signed and stacked flows, dual-axis comparisons, seasonal overlays, yield curves, heatmaps, instrument tables, and shareable chart-card PNGs; not for general non-chart UI."
license: MIT
metadata:
  author: KaigorodovTuskul
  version: "0.2.0"
  status: reference-based
---

# Simulacre Financial Charts

Build a chart that answers **one financial question** while preserving the underlying measurement and time semantics. The skill is a pattern/QA guide, not a live data source or mandatory rendering engine.

## Activation and limits

Use when choosing, implementing, evaluating, redesigning or exporting financial and macroeconomic charts. For general page design without data visualization, do not activate. Never fabricate observations, source names, performance figures, or an exact CSS token value absent evidence. Preserve explicit user requirements and the host application's design system when the user asks for integration rather than Simulacre styling.

## Operating sequence

1. **Frame:** State the question, audience, units, frequency, latest *observation* date, *release* date (if different), and whether the series is a level, rate, change, flow, spread, index or cross-section. If unknown and decision-changing, ask.
2. **Select:** Consult [pattern catalog](references/simulacre-v1-pattern-catalog.md) and, for known indicators, [machine-readable inventory](references/indicator-catalog.json). Prefer semantics over historical template labels.
3. **Implement:** Use a stable chart shell: title, as-of date, up to 3–4 meaningful KPIs, chart, source/attribution and optional watermark. Maintain a dominant primary series and a readable small-screen layout.
4. **Verify semantics:** Check [financial semantics](references/financial-semantics.md): denominators, units, zero baselines, date alignment, revisions, gaps, seasonality, sign, polarity and secondary axes.
5. **Verify visuals:** Inspect actual rendered states at desktop and narrow widths. Check labels, clipping, contrast, legends and interaction; use captured [reference images](references/reference-manifest.json) as examples, not proof of correctness.
6. **Export:** If asked to export, read [capture and export](references/capture-and-export.md). Wait for chart *content*, not just a DOM element, and validate the real downloadable artifact. Explicitly report fallback or failure.

## Pattern rules

- **Line:** continuous levels, rates, indices and comparable time-series. Make a benchmark or prior period visually secondary. Do not join actual observations across genuinely missing periods without disclosure.
- **Signed bar:** periodic change, balance, net flow or surprise. Anchor at zero; encode direction consistently, but do not automatically equate green with economically favorable.
- **Stacked bars:** only components that add to a meaningful total, with a clearly defined handling of signed stacks and missing components.
- **Dual-axis bar + line:** different units with common time alignment only; label both axes prominently. Prefer normalized comparable series or separate panels if the second axis invites false correlation.
- **Seasonal overlay:** align by defined week or month position, explicitly handle ISO week 53, leap days, partial current periods and differing reporting calendars.
- **Yield scatter/bubbles:** maturity on x, yield on y; encode size and color separately and supply their legends. Do not connect separate bonds as if they formed a historical series.
- **Market heatmap:** use group labels, explicit change units and a neutral midpoint. Tile area is not market capitalization unless deliberately encoded as such.
- **Sortable table:** prioritize decision-critical columns, repeat units in headings and avoid fake precision.

## Visual decisions

- Data fidelity outranks matching pixels. Preserve the actual displayed values and avoid invented latest points or zeros for missing observations.
- Only use one unit per axis. Tooltips must identify series, observation date, exact value and unit; static export must expose enough information to stand alone.
- Red/green may represent positive/negative **numeric direction**, not investment advice or necessarily economic goodness. Use labels, position or symbols in addition to color.
- A dark interactive UI and light report PNG may require separate palettes; observed [design tokens](references/design-tokens.json) are approximate samples, **not authoritative CSS**.
- Keep text and annotations inside the plotting bounds; reserve headroom for highest-bar labels and preserve legends and sources in exported images.

## Release gates

- **DATA:** actual vs forecast, frequency, timezone, date alignment, revisions, missing observations, signs, decimal places and source evidence are consistent.
- **VISUAL:** axes, baseline, nonclipped annotations, readable legend, contrast, hover/focus and narrow layout have been checked.
- **EXPORT (if requested):** render-ready gate passed, real PNG action succeeded, image dimensions/content were inspected, and screenshots are not misrepresented as application exports.

If a gate fails, fix it or describe the limitation; never claim validation that was not performed. Don't run a large browser benchmark or visual regression suite for a simple textual chart recommendation.
