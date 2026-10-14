# Simulacre v1 pattern catalog

Research basis: October 2026 public macro dashboard at `https://simulacre-ai.ru/site/`, its Playwright-captured PNGs, and implementation map in `moex_ai_mcp`. The original source inventory contained **53 indicators**. For the complete, normalized and machine-checkable inventory see [`indicator-catalog.json`](indicator-catalog.json).

**A source renderer/template is not necessarily the user's active chart type.** An indicator can have multiple tabs (e.g., bond tables and yield scatters) or specialized layouts. Choose from the active question, units and data semantics.

## Reusable patterns

| Pattern | Best analytical question | Reference indicator | Image |
| --- | --- | --- | --- |
| Report card + KPIs | What moved, when, and by how much? | All | Curated assets in `../assets/reference-charts/` |
| Line / comparable series | How has a rate, index or spread evolved? | `global_dxy` | `global-dxy.png` |
| Signed periodic bars | What changed each reporting period? | `russia_cpi_mom` | `russia-cpi-mom.png` |
| Stacked bars + line | How do components and another level move? | `russia_carry_trade_monitor` | `russia-carry-trade-monitor.png` |
| Seasonal overlay | Is the current week unusual versus past years? | `russia_weekly_cpi` | `russia-weekly-cpi.png` |
| Yield / maturity scatter | How do bonds cluster by yield, tenor and liquidity? | `russia_ofz_yield_curve_monitor` | `russia-ofz-yield-curve-monitor.png` |
| Grouped heatmap | Which assets or markets changed most? | `global_market_heatmap` | `global-market-heatmap-fallback.png` |
| Instrument table | Which issues explain the aggregate? | `russia_rgbi_ofz_constituents` | `russia-rgbi-ofz-constituents-fallback.png` |

Both `*-fallback.png` images are **element screenshots following failed browser exports**, not successful PNG-button results. Details in [capture-and-export](capture-and-export.md).

## Historical source-template inventory

This grouping describes the application's original **top-level** source templates. It is not a complete description of each chart tab. The JSON catalog preserves the exact list and tab-specific overrides.

- **Line / multi-series / rate and spread (25):** `imoex_market_breadth`, `russia_tax_period_fx_pressure`, `russia_rgbi_ofz_constituents`, `russia_ofz_yield_curve_monitor`, `russia_fx_share_broad_money`, `russia_m2_cpi_spread_monitor`, `russia_ruble_deposit_structure`, `russia_budget_rule_oil_gap`, `russia_usdrub_cross_monitor`, `global_dxy`, `russia_cpi_saar_monitor`, `cbonds_key_rate_curve_monitor`, `moex_key_rate_futures`, `moex_rusfar_curve_monitor`, `russia_ruonia_rusfar_spread`, `moex_rgbi`, `frg100_deposits`, `russia_cpi_yoy`, `russia_inflation_expectations`, `russia_business_price_expectations`, `russia_manufacturing_pmi`, `russia_services_pmi`, `russia_business_confidence`, `russia_weekly_cpi`, `russia_ofz_26243_26233_spread`.
- **Ordinary bars / flow bars (18):** `russia_fund_flows_monitor`, `russia_m2_inflation_pressure`, `russia_minfin_fx_pressure_monitor`, `russia_cbr_repo_auctions`, `russia_cpi_mom`, `russia_unemployment_rate`, `russia_trade_balance`, `russia_fx_reserves`, `russia_monthly_gdp`, `russia_quarterly_gdp`, `russia_budget_balance_gdp`, `russia_ppi_mom`, `russia_ppi_yoy`, `russia_forex_intervention`, `russia_retail_sales_yoy`, `russia_industrial_production_yoy`, `russia_real_wage_growth_yoy`, `russia_minfin_nwf_monitor`.
- **Signed delta bars (5):** `russia_minfin_fx_actual_flow`, `russia_minfin_fx_regular_flow_est`, `russia_minfin_fnb_adjustment_est`, `russia_ruble_liquidity`, `russia_bank_liquidity_balance`.
- **Stacked composition (4):** `russia_carry_trade_monitor`, `russia_capital_flows_by_participant`, `russia_minfin_ofz_auctions`, `russia_oil_exports_crea`.
- **Market scan (1):** `global_market_heatmap`.

## Visual conventions observed from captured PNGs

- A light export surface, red accent rule, bold title, as-of date, compact KPI row, source and `@simulacre_ai_bot` attribution.
- Low-contrast grid and secondary series, with a dominant primary series.
- A bond bubble's size, color and coordinates represent different measures. A heatmap's color encodes numeric direction; tile area must not accidentally imply capitalization.
- **Known counterexamples to avoid:** labels clipping near maximum bars; DOM-only panels cropped by scrollbars; ambiguously favorable-looking green deltas on inflation cards.

Measured export-surface colors and limitations: [design-tokens.json](design-tokens.json). Use [financial semantics](financial-semantics.md) before adopting visual conventions.
