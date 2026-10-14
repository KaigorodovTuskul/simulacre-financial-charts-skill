# Simulacre v1 pattern catalog

Research date: 2026-10-15. Source: the public macro dashboard at `https://simulacre-ai.ru/site/`, its exported PNGs, and the corresponding implementation in `moex_ai_mcp`.

The source catalog contained 53 indicators. The main renderer exposes five top-level templates, but some indicators provide chart tabs whose visual type differs from the catalog default. Select the pattern from the active question and data semantics, not from a historical template label.

## Reusable patterns

| Pattern | Best question | Reference indicator | Visual evidence |
| --- | --- | --- | --- |
| Card shell + KPI strip | What changed, when, and by how much? | All charts | Every PNG in `../assets/reference-charts/` |
| Line / comparable series | How is a level, rate, or spread evolving? | `global_dxy` | `global-dxy.png` |
| Signed periodic bars | What was the period-on-period move? | `russia_cpi_mom` | `russia-cpi-mom.png` |
| Stacked bars + right-axis line | How do additive components and a market level move together? | `russia_carry_trade_monitor` | `russia-carry-trade-monitor.png` |
| Seasonal year overlay | Is the current calendar position unusual versus comparable years? | `russia_weekly_cpi` | `russia-weekly-cpi.png` |
| Yield-curve bubbles | How are yield, maturity, liquidity, and day move distributed across bonds? | `russia_ofz_yield_curve_monitor` | `russia-ofz-yield-curve-monitor.png` |
| Grouped market heatmap | Where is the market move concentrated right now? | `global_market_heatmap` | `global-market-heatmap-fallback.png` |
| Sortable instrument table | Which instruments explain the aggregate? | `russia_rgbi_ofz_constituents` | `russia-rgbi-ofz-constituents-fallback.png` |

## 53-indicator inventory

### Line / multi-series / rate and spread views (25)

`imoex_market_breadth`, `russia_tax_period_fx_pressure`, `russia_rgbi_ofz_constituents`, `russia_ofz_yield_curve_monitor`, `russia_fx_share_broad_money`, `russia_m2_cpi_spread_monitor`, `russia_ruble_deposit_structure`, `russia_budget_rule_oil_gap`, `russia_usdrub_cross_monitor`, `global_dxy`, `russia_cpi_saar_monitor`, `cbonds_key_rate_curve_monitor`, `moex_key_rate_futures`, `moex_rusfar_curve_monitor`, `russia_ruonia_rusfar_spread`, `moex_rgbi`, `frg100_deposits`, `russia_cpi_yoy`, `russia_inflation_expectations`, `russia_business_price_expectations`, `russia_manufacturing_pmi`, `russia_services_pmi`, `russia_business_confidence`, `russia_weekly_cpi`, `russia_ofz_26243_26233_spread`.

Notes: `russia_weekly_cpi` is a seasonal overlay indexed by week number; `russia_ofz_yield_curve_monitor` uses a scatter/bubble chart in its active view; `russia_rgbi_ofz_constituents` exposes a table and a yield scatter through chart tabs.

### Ordinary bars / flow bars (18)

`russia_fund_flows_monitor`, `russia_m2_inflation_pressure`, `russia_minfin_fx_pressure_monitor`, `russia_cbr_repo_auctions`, `russia_cpi_mom`, `russia_unemployment_rate`, `russia_trade_balance`, `russia_fx_reserves`, `russia_monthly_gdp`, `russia_quarterly_gdp`, `russia_budget_balance_gdp`, `russia_ppi_mom`, `russia_ppi_yoy`, `russia_forex_intervention`, `russia_retail_sales_yoy`, `russia_industrial_production_yoy`, `russia_real_wage_growth_yoy`, `russia_minfin_nwf_monitor`.

### Signed delta bars (5)

`russia_minfin_fx_actual_flow`, `russia_minfin_fx_regular_flow_est`, `russia_minfin_fnb_adjustment_est`, `russia_ruble_liquidity`, `russia_bank_liquidity_balance`.

### Stacked bars / composition (4)

`russia_carry_trade_monitor`, `russia_capital_flows_by_participant`, `russia_minfin_ofz_auctions`, `russia_oil_exports_crea`.

### Market scan (1)

`global_market_heatmap`.

## Composition conventions observed

- The card is the unit of sharing: red accent rule, bold title, top-right as-of date, compact KPI row, chart, source, and `@simulacre_ai_bot` watermark.
- Charts use a light report surface in PNG even though the interactive site supports dark UI. Gridlines are thin and low-contrast; labels are compact.
- The primary series is distinguished by stronger red or dark line weight. Benchmarks use muted gray or purple dashes.
- The graphical details must follow data semantics: e.g. green/red tiles in the heatmap represent percent direction, while a bond bubble’s size represents weight/liquidity and color represents daily price move.
