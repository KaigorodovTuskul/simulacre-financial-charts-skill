# Browser capture and PNG export protocol

Audit basis: October 2026 public [Simulacre AI macro dashboard](https://simulacre-ai.ru/site/) and source-code mapping from the original project. The observed application uses Chart.js 4 in the browser and a separate Matplotlib route for deterministic report exports. This repository does not ship either implementation.

| Responsibility | Observed original source location |
| --- | --- |
| Chart.js import and page shell | `apps/site/index.html` |
| Interactive chart card, controls and special DOM modes | `apps/site/js/macro.js` |
| Template, data and axis metadata | `src/web/macro_service.py` |
| Server report renderer | `src/web/report_exports.py` |
| Responsive card styling | `apps/site/css/app.css` |

The observed frontend dispatch includes `line`, `bar`, `delta_bar`, `stacked_bar`, `flow_bar`, `market_heatmap`, `rgbi_bond_table`, `rgbi_yield_scatter`, `expert_views` and `futoi_table`.

## Render-ready gate (required for browser automation)

The first batch captured 12 identical blank chart shells because the export action was triggered **before** the cards finished rendering. Re-exporting after actual content appeared produced 12 unique nonblank files. This is a diagnosed timing race, not evidence of intrinsic renderer failure.

A gate must assess the **specific card** being exported; do not use a global `networkidle`, sleep or generic canvas presence as the only success criterion.

1. Navigate/select the requested indicator and correct tab.
2. Wait for the **expected chart title**, visible and non-placeholder KPIs (when present), and its data-rendering surface (`canvas` or actual DOM tiles/table).
3. For canvas charts, wait for chart initialization and at least one rendered dataset/valid mark; where Chart.js is used, read its chart instance/dataset metadata if available. A nonzero canvas width alone is insufficient.
4. For DOM widgets, verify meaningful visible rows/tiles and no loading or empty-state overlay. For nontrivial animations, disable them in test mode or wait for completion.
5. Wait for layout stability over at least two animation frames; capture a pre-export screenshot for traceability.
6. Click the application's actual PNG action. Capture the download or actionable export error. Check MIME/PNG signature, dimensions, nonblank chart region, required title/KPI/source/watermark regions where applicable, and plausible content.
7. Record a per-indicator status and artifact reference; never call a failed export a successful PNG button test.

Example Playwright **pseudocode** (adapt the locators and `hasRenderedData` implementation to the app; these are not verified selectors):

```js
const card = page.locator('[data-indicator-id="YOUR_ID"]');
await card.getByRole('heading', { name: /expected title/i }).waitFor();
await page.waitForFunction(() => window.hasRenderedData?.('YOUR_ID') === true);
const downloadPromise = page.waitForEvent('download');
await card.getByRole('button', { name: /png|export/i }).click();
const download = await downloadPromise;
await download.saveAs('output.png');
// Now inspect decoded PNG content, not just the filename or hash.
```

An implementation need not use the example hook; inspect real Chart.js state, SVG marks, DOM data rows, or application-specific render-complete events instead. Watch for dynamic lazy loading on scroll, font loading, and active chart tabs. A no-timeout wait can hang; set a reasonable deadline and log failures.

## Export outcomes

| Status | Meaning |
| --- | --- |
| `VALID_EXPORT` | Application action completed and a content-complete image was inspected |
| `BLANK_EXPORT` | PNG exists but expected chart content is missing |
| `FAILED_EXPORT` | Application action failed, or file cannot be decoded |
| `FALLBACK_SCREENSHOT` | Element/page screenshot after failure, *not* a successful export |
| `NOT_TESTED` | No evidence of an attempted export |

**Hashes, image size and uniqueness are smoke checks, not correctness proof.** Compare a rendered image to known chart elements, data values and source metadata. When reference data changes, compare semantic properties rather than pixel-perfect content.

## Remaining distinct defect: DOM export / tainted canvas

On 2026-10-15, the original PNG action failed for `global_market_heatmap` and `russia_rgbi_ofz_constituents` with `SecurityError: Failed to execute 'toBlob' on 'HTMLCanvasElement': Tainted canvases may not be exported.` Their stored `*-fallback.png` files are element screenshots. The timing-race fix for the other 12 exports **does not fix this CORS/tainted-canvas failure**.

To fix a DOM-to-canvas route, keep source assets origin-clean (same-origin/CORS-enabled resources, correctly loaded fonts and SVG styles), or use a deterministic server renderer. Handle `toBlob` rejections and null blobs explicitly. Do not bypass browser origin protection; do not conceal that a screenshot was substituted.

## Reference provenance and privacy

The local Playwright archive may contain unrelated site visits, authentication/OAuth URLs or debugging logs. **Never commit it wholesale**. Whitelist the intended chart PNGs, redact all tokens and identifiers, and retain only public non-sensitive metadata. This repository preserves seven selected visual references; it does not commit the full 53-capture archive.
