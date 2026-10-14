---
name: simulacre-financial-charts
description: "Design, implement, review, or export decision-grade financial and macroeconomic charts. Use for market-data visualizations including time-series lines, signed and stacked flows, dual-axis comparisons, seasonal overlays, yield curves, heatmaps, instrument tables, and shareable chart-card PNGs; not for general non-chart UI."
license: MIT
metadata:
  author: KaigorodovTuskul
  version: "0.1.0"
  status: reference-catalog
---

# Simulacre Financial Charts

Create a chart that answers one financial question at a glance. Prefer the smallest truthful visual over a dense dashboard.

## Default workflow

1. Identify the decision question, observation frequency, units, and the primary series.
2. Choose a pattern from [the Simulacre pattern catalog](references/simulacre-v1-pattern-catalog.md). Do not select a chart type because it is visually familiar.
3. Keep the primary series visually dominant; put the latest value, period, and meaningful delta in the card shell.
4. Verify zero baselines for bars, axis units, date alignment, missing-value treatment, series order, and tooltip values.
5. Validate the rendered chart at desktop and narrow widths. If it is exported, test the actual PNG action as well as the interactive view.

## Pattern selection

- Use a **line** for a continuous level, rate, spread, index, or comparable time series. Use a dashed line only for a benchmark, history, forecast, or comparison series.
- Use a **signed bar** for periodic change, net flow, balance, or surprise. Anchor it at zero and encode sign with green/red only when that semantic is stable in context.
- Use a **stacked bar** only when components add to a useful total. Do not stack unrelated series merely to save space.
- Use **bar + line with a right axis** only for two different units sharing the same time context (for example, turnover plus FX level). Name both units clearly; avoid a second axis when normalization would answer the question better.
- Use a **seasonal overlay** when matching positions in a calendar cycle is the question. Align by week or month number, label the current year clearly, and use the current year's calendar date only in the surrounding card.
- Use a **scatter / bubble yield curve** for cross-sectional instruments: x = maturity, y = yield, bubble size = liquidity or weight, color = a separate directional measure. Never imply chronology with a connecting line unless the curve is explicitly interpolated.
- Use a **heatmap** for a broad market scan. Group tiles by asset class, sort within a group by change, and do not make tile area imply value unless area is intentionally encoded.
- Use a **sortable table** when the user must inspect instruments rather than a single relationship. Keep the first visible columns decision-critical and use inline progress only for true part-to-whole fields.

## Visual rules carried from the Simulacre reference set

- Build each shareable view as a card: title and as-of date, at most 3–4 KPI cards, one chart, source, and watermark. More panels need separate tabs, not a smaller chart.
- Preserve stable series colors across tabs. Make the primary series stronger (line width or saturation); comparisons are lower contrast.
- Limit date ticks; use compact, locale-aware labels. Annotate only the last point by default, or every bar only when there are few enough observations to read.
- Plot raw values unless normalization directly answers the question. Never mix different units on one axis.
- Tooltips must expose the exact value, unit, observation date, and series name. Legends must match visual order.
- Treat missing observations as gaps, not zeros. Do not manufacture a latest point merely to extend a chart.
- Avoid decorative gradients, 3D effects, and animations that alter the reading of the data. Motion, if any, should only aid orientation.

## Implementation and export checks

For the source implementation and its observed export behavior, read [capture and export notes](references/capture-and-export.md). For the code-to-pattern inventory of all 53 reference indicators, read [the catalog](references/simulacre-v1-pattern-catalog.md).

Before declaring a chart finished, use this checklist:

- Does the chart answer its title without relying on prose?
- Are dates, week numbers, and release/as-of dates semantically distinct and displayed correctly?
- Does every color, axis, and bar baseline have one unambiguous meaning?
- Is the latest datapoint factual rather than a placeholder or extrapolation?
- Does the download/export result contain the same information as the visible card?
