# Financial and macroeconomic data semantics

Treat this as a **data correctness** gate. A visually faithful chart may still be wrong.

## Measurement before drawing

| Input | Required clarification | Frequent failure |
| --- | --- | --- |
| Level or index | base year, nominal/real, seasonally adjusted? | plotting index levels as percentages |
| MoM / QoQ | rate convention, NSA/SA, percentage vs percentage points | replacing percentage-point change with percent growth |
| YoY | same comparable period and measurement vintage | labeling an annualized month-on-month change as YoY |
| SAAR | seasonally adjusted annualized rate and compounding convention | silently multiplying the monthly percentage by 12 |
| Spread | minuend, subtrahend, bps vs percentage points | swapping sign or mixing bps with p.p. |
| Flow | interval covered and signed convention | drawing period flows as cumulative stock |
| Stock | point-in-time date and currency | showing a balance as if it were a period flow |
| Inflation | price index vs rate of price change | treating a higher rate as universally favorable |
| Yield curve | as-of snapshot, maturity/tenor, bid/ask/yield convention | implying a time path from unrelated bonds |

## Time

- Distinguish **observation date**, **publication/release timestamp** and **chart as-of timestamp**. Real-time macro data may be revised after publication: state vintage when material.
- Series with different frequencies must be aligned with an explicit policy (e.g., latest available by publication date). Do not create intermediate observations by forward fill without labeling the result.
- Weekly comparisons must choose a convention (ISO-8601 week vs release week vs statistical reporting week). Weeks 52/53 and leap years require explicit handling; current-year partial weeks must not be treated as complete.
- Trading days and weekends differ from statistical-release calendars. Point gaps are gaps, not zero events. A latest observation may precede the current date.
- Cross-country overlays may have different seasonal adjustment and reporting lags. Do not present them as directly comparable without qualifying differences.

## Units and baselines

- For bar magnitude comparisons use zero as a baseline. Signed flows and negative values need visible zero and a stable sign convention.
- For rates and levels, a nonzero y-axis range may be appropriate, but it must not suggest a different scale or exaggerate a claimed effect.
- Percent (`%`), percentage points (`p.p.`), basis points (`bp`), currency, quantity and index points are distinct and never share an unlabeled axis.
- Make nominal/real values, FX conversions, denominators and rolling-window definitions visible when decision-relevant.

## Direction, sentiment and interpretation

Never infer the *economic meaning* of a sign from its visual direction alone. Rising inflation, higher borrowing costs, rising credit spreads and lower unemployment mean different things. Store or describe three independent fields: `change_sign`, `semantic_polarity` (favorable, unfavorable, mixed, neutral, unknown) and `comparison_baseline`. For uncertain or contested interpretation, keep color neutral and explain rather than assign red/green endorsement.

## Charts with multiple variables

A dual-axis chart is not evidence of causality. Consider small multiples, indexing to a common base or showing a spread where valid. For a bubble chart, disclose whether size means capitalization, weight or liquidity, and whether x-axis uses time to maturity or duration. For a heatmap, state what determines tile size and sorting, and choose a neutral color around no change.

## Export completeness

A standalone exported chart needs an explanatory title, data units, source, relevant time reference and legends. Tooltips alone are insufficient because they disappear from PNG. Reject data labels outside the export bounds and chart cards with a blank underlying series.
