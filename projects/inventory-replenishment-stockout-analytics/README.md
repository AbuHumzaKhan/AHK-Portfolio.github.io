# Inventory Replenishment & Stockout Analytics

Portfolio project by Abu Humza Khan | Python, SQL, Excel, HTML dashboard

## Business question
Where does a simulated inventory network miss demand, and which product categories, warehouses, and SKUs should operations review first? The project pairs unit fill rate with stockout-day frequency and purchase-order timing so a high aggregate service level does not hide localized issues.

## Scope and data provenance
- Deterministic synthetic scenario generated with NumPy seed 20261023.
- 36 SKUs, 5 product categories, 3 warehouses, and 90 daily observations from 2026-07-03 through 2026-09-30.
- 9,720 inventory snapshots at one row per date × SKU × warehouse, plus simulated purchase orders.
- No external or proprietary data, no paid API, and no personal data.
- Run the Python pipeline to generate the full CSV datasets, SQLite database, Excel workbooks, QA results, findings, charts, and dashboard.

## Initial findings (synthetic scenario)
- Demand: 138,329 units; fulfilled: 136,221; unmet: 2,108.
- Unit fill rate: 98.48%; stockout-day rate: 2.19%.
- Potential lost sales value: INR 3,261,211.31. This is unmet units × synthetic list price, not booked revenue or a forecast.
- Ending on-hand inventory value: INR 13,488,172.55.
- 747 purchase orders; 687 received within the observation window; 62.30% on-time among received orders.
- Sports has the highest category stockout-day rate (2.75%); North Hub has the lowest fill rate (97.61%); SKU-033 (Skipping Rope) has the highest unmet volume (220 units).

These are generated scenario results, not conclusions about a real supply chain. The replenishment rules are heuristics and the 20% annual carrying-cost rate is an illustrative assumption.

## Tool stack and deliverables
- Python: synthetic data generation, analysis, report generation, and automated QA.
- SQL / SQLite: schema, generated dimension seed data, business queries, indexes, and QA queries.
- Excel 2019-compatible workbooks: formula-driven KPIs, category and warehouse summaries, and charts.
- HTML dashboard with SVG charts, plus PNG report charts.
- Unit tests and dated change log.

A native Power BI PBIX is not included. The dashboard deliverable is HTML.

## Run locally
1. Create and activate a Python virtual environment.
2. Install dependencies with: pip install -r requirements.txt
3. Run the pipeline with: python -m src.run_pipeline
4. Run tests with: python -m unittest discover -s tests -v
5. Open reports/inventory_dashboard.html in a browser.

The pipeline rebuilds only the SQLite database in this project directory. It does not modify other projects. Excel formulas recalculate when opened in Excel or LibreOffice; openpyxl does not calculate formula results itself.

## Key files
- src/: modular synthetic-data pipeline, analytics, SQL loading, Excel reporting, dashboard generation, and QA.
- sql/: schema, seed data, business queries, and QA checks.
- docs/: data dictionary, provenance, methodology, assumptions, and deployment instructions.
- reports/: browser dashboard and SVG/PNG charts.
- outputs/: findings, metrics, and validation results.
- tests/: repeatable automated tests.

## Limitations
Lost demand is treated as lost sales. Returns, backorders, transfers, promotions, shrinkage, taxes, and financing are excluded. Potential lost sales value is a proxy. No causal claims are made. Review docs/assumptions_and_limitations.md before adapting the model to real data.

## Credits
Created by: Abu Humza Khan
GitHub profile: https://github.com/AbuHumzaKhan
LinkedIn profile: https://www.linkedin.com/in/abu-humza-khan/
Source: ChatGPT
Design Idea: ChatGPT
