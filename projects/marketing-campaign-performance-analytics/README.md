# Marketing Campaign Performance & Budget Efficiency Analytics

A reproducible marketing analytics case study built with Python, SQL/SQLite, Excel, Power BI assets, and a self-contained HTML dashboard.

> **Data notice:** All records and monetary values are synthetic and illustrative. The scenario was generated with seed 20261026 and covers 6 July–27 September 2026. It is not sourced from a real advertiser or ad platform.

## Business problem

Marketing stakeholders need to compare spend, attributed conversion value, acquisition cost, and channel efficiency without treating high volume as proof of profitability. This project standardizes those KPIs across SQL, Excel, and Power BI and highlights where controlled follow-up tests may be useful.

## Scenario scorecard

| KPI | Result |
|---|---:|
| Campaign-day rows | 672 |
| Campaigns / channels | 8 / 6 |
| Impressions | 14,425,535 |
| Clicks | 339,089 |
| Click-through rate | 2.35% |
| Modeled spend | $250,684.98 |
| Simulated conversions | 17,298 |
| Attributed conversion value | $1,451,894.37 |
| Cost per acquisition | $14.49 |
| Portfolio ROAS | 5.79x |
| Spend / planned budget | 83.83% |

The highest modeled channel ROAS is Email at 17.26x. Lifecycle Email also has the lowest simulated CPA at $4.00, while Generic Search has the largest spend allocation at $90,434.04. These are synthetic scenario findings, not instructions to shift real budgets.

## Included assets

- Python generator and KPI analysis script.
- SQLite schema, reproducible seed-data generator, business queries, and SQL QA checks.
- Excel workbook in the downloadable bundle, with formulas, campaign/channel summaries, filters, and charts.
- Power BI DAX measures, Power Query M, model instructions, and a report preview.
- Interactive HTML dashboard and static dashboard preview.
- Data dictionary, initial findings, validation summary, and dated changelog.

**Native Power BI .pbix:** not generated. The supplied DAX/M/model assets are implementation materials; the HTML dashboard is the immediately viewable report.

## Reproduce

From the project root, with Python 3.10+:

    python python/generate_data.py
    python python/analyze_campaigns.py
    python -m unittest discover -s tests -v

The generator uses only the Python standard library and recreates the CSVs, SQL seed data, and SQLite database. Run the SQL business queries against the generated database. Open the Excel workbook in Excel 2019 or later and allow formulas to recalculate. Open reports/dashboard_preview.html for the static preview; the full downloadable bundle contains the interactive reports/dashboard.html.

## Validation

The local build passed 19 data/workbook/asset QA checks. The reproducible Python test suite passed 12 tests with zero failures, including row grain, date range, metric bounds, campaign coverage, SQLite integrity and reconciliation, SQL QA, business-query execution, and metric JSON reconciliation.

## Stakeholder recommendations

1. Treat high-ROAS channels as candidates for controlled tests, not automatic scale-up targets.
2. Review high-spend campaigns with below-portfolio ROAS and inspect weekly marginal returns.
3. Compare CPA with conversion rate, conversion count, and order value before reallocating budgets.
4. Validate platform billing, attribution windows, refunds, gross margin, and incrementality before operational use.
5. Retain a holdout or geo experiment where feasible to estimate incremental lift.

## Assumptions and limitations

- All activity and monetary values are simulated; patterns are partly built into campaign-specific assumptions.
- Attributed value is not audited net revenue or profit.
- ROAS does not establish causal impact or incremental lift.
- No customer-level identity, multi-touch attribution, refunds, margins, or live platform integration is included.
- Email impressions and costs are modeled proxies that may not match platform definitions.

## Change log

**2026-10-26 — Initial release:** synthetic dataset, Python pipeline, SQLite schema/seed/queries, Excel workbook, HTML dashboard, Power BI assets, QA evidence, data dictionary, and stakeholder findings.

## Credits

Created by: Abu Humza Khan  
GitHub profile: https://github.com/AbuHumzaKhan  
LinkedIn profile: https://www.linkedin.com/in/abu-humza-khan/  
Source: ChatGPT  
Design Idea: ChatGPT