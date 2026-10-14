# Example prompts

## Weekly CPI seasonal comparison

> Use simulacre-financial-charts to show weekly Russian inflation against historical weeks. Use one explicitly defined week calendar, mark unavailable weeks as gaps, distinguish observation from release dates and avoid treating a partial week as complete. Export a standalone readable PNG.

## OFZ yield cross-section

> Build a scatter plot for OFZ issues: time to maturity on X, yield on Y, bubble size for a specified liquidity proxy, color for daily price direction. Include a full size legend and don't connect individual issue dots into a misleading time series.

## Two-unit market monitor

> Compare an FX level and intervention flow. Decide if a dual-axis combination is justified or if aligned small multiples avoid misleading correlation. Label flow units, periods and timezones, and explain your choice.

## Export QA

> Inspect my existing Chart.js financial chart and its PNG button. Test the real UI, wait for rendered data rather than only a canvas DOM node, and report whether the file is a valid app export, a fallback screenshot or a failed/blank export.
