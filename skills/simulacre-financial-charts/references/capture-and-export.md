# Capture and export notes

## Observed implementation map

The audited application uses Chart.js 4 in the browser and a separate Matplotlib path for deterministic report exports.

| Responsibility | Source location |
| --- | --- |
| Chart.js import and macro page shell | `apps/site/index.html` |
| Interactive card, controls, Chart.js datasets and DOM special modes | `apps/site/js/macro.js` |
| Data templates, series metadata, axis/style choices | `src/web/macro_service.py` |
| Server-side report rendering | `src/web/report_exports.py` |
| Card/grid/responsive styling | `apps/site/css/app.css` |

`macro.js` dispatches `line`, `bar`, `delta_bar`, `stacked_bar`, `flow_bar`, `market_heatmap`, `rgbi_bond_table`, `rgbi_yield_scatter`, `expert_views`, and `futoi_table`. Series metadata provides the reusable primitives: primary series, preferred color, line/dashed style, left/right axis, point-only mode, and stack group.

## Export protocol

1. Render the exact card that the user sees, including title, as-of date, KPIs, chart, source, and watermark.
2. Exercise the real PNG action. A screenshot alone proves appearance but not exportability.
3. If the page includes DOM-only modules (tables or tile heatmaps), test them specifically; canvas export often differs from Chart.js canvas export.
4. If browser export fails, use a deterministic server-side renderer or a clearly labelled screenshot fallback. Never silently deliver a blank export.

## Observed failure to guard against

On 2026-10-15, the public PNG action failed for `global_market_heatmap` and `russia_rgbi_ofz_constituents` with `SecurityError: Failed to execute 'toBlob' on 'HTMLCanvasElement': Tainted canvases may not be exported.` The audit saved element screenshots as `*-fallback.png` for visual reference. They are not successful button exports.

Guardrails:

- Keep exported canvases origin-clean; use CORS-enabled assets or inline styles/assets in the SVG-to-canvas path.
- Detect a null blob or rejected `toBlob` call and show an actionable failure state.
- For critical reports, prefer the server-side renderer because it is deterministic and avoids browser CORS state.
