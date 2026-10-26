# Validation Summary — 26 October 2026

- Data QA checks: 19/19 passed during local build.
- Python unit tests: 12 passed, 0 failures.
- Row count and grain: 672 unique date/campaign combinations.
- Dimensions: 8 campaigns and 6 channels.
- Date range: 2026-07-06 through 2026-09-27.
- Constraints: clicks never exceed impressions; numeric metrics are non-negative.
- Database: SQLite integrity and foreign-key checks passed.
- Reconciliation: CSV totals match SQLite and metrics_summary.json.
- SQL: all QA checks returned zero failures; all six business queries executed successfully.
- Excel: formulas, four worksheets, and three charts were inspected structurally; Excel recalculation should be confirmed on open.
- Dashboard: HTML and SVG assets verified locally.

The native Power BI .pbix was not generated. Hosted deployment has not been verified.