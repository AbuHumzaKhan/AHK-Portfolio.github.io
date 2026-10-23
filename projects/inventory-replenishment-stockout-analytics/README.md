# Inventory Replenishment & Stockout Analytics

**Portfolio project by Abu Humza Khan | Python + SQL + Excel**

This folder is the public portfolio showcase for a reproducible inventory analytics project. The complete project bundle delivered with this conversation includes the full synthetic dataset, SQLite database, Python pipeline, both Excel workbooks, dashboard assets, documentation, and tests. A standalone repository could not be created through the connected GitHub operations, so the public showcase is hosted inside the existing portfolio website repository.

## Business question
Where does a simulated inventory network miss demand, and which product categories, warehouses, and SKUs should operations review first? The project pairs unit fill rate with stockout-day frequency and purchase-order timing so an aggregate service metric does not hide localized issues.

## Data provenance
All data is synthetic and generated with a fixed seed (20261023): 36 SKUs, five product categories, three warehouses, 90 daily observations from 2026-07-03 through 2026-09-30, and 9,720 inventory snapshots. No external or proprietary data and no personal data are used.

## Results from the generated scenario
- Demand: 138,329 units; fulfilled: 136,221; unmet: 2,108.
- Unit fill rate: 98.48%; stockout-day rate: 2.19%.
- Potential lost sales value: INR 3,261,211.31. This is unmet units × synthetic list price, not booked revenue or a forecast.
- Ending on-hand inventory value: INR 13,488,172.55.
- 747 purchase orders; 687 received in the observation window; 62.30% on-time among received orders.
- Sports has the highest category stockout-day rate (2.75%); North Hub has the lowest fill rate (97.61%); SKU-033 (Skipping Rope) has the highest unmet unit volume (220 units).

These are generated scenario outputs, not conclusions about a real supply chain. The replenishment rules are heuristics, and the 20% annual carrying-cost rate is illustrative.

## Public showcase assets
- Dashboard: reports/inventory_dashboard.html
- Initial findings: outputs/INITIAL_FINDINGS.md
- Metrics and QA: outputs/PROJECT_METRICS.json and outputs/qa_checks.csv
- SQL schema and business queries: sql/
- Data dictionary, provenance, methodology, limitations, and deployment notes: docs/

## Run the complete project locally
Use the complete downloadable project ZIP provided with this conversation. Extract it, create a Python virtual environment, install requirements.txt, run python -m src.run_pipeline, then run python -m unittest discover -s tests -v. The pipeline recreates the full dataset, SQLite database, Excel reports, dashboard, findings, and QA outputs.

## Limitations
Unmet demand is treated as lost sales. Returns, backorders, transfers, promotions, shrinkage, taxes, and financing are excluded. Potential lost sales value is a proxy. Category and warehouse differences are not causal evidence. Review docs/assumptions_and_limitations.md before adapting the model to real data.

## Credits
Created by: Abu Humza Khan
GitHub profile: https://github.com/AbuHumzaKhan
LinkedIn profile: https://www.linkedin.com/in/abu-humza-khan/
Source: ChatGPT
Design Idea: ChatGPT
