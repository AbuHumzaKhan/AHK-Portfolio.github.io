# Build Audit — Healthcare Appointment Access & No-show Analytics

**Audit date:** 2026-10-29

## Domain and tool-selection rationale
The preceding portfolio project was marketing campaign performance. This release rotates to healthcare operations analytics and uses Python + SQL/SQLite + Excel + a local HTML dashboard. All healthcare-related records are synthetic; no patient-identifiable information is included.

## Build inventory
- Fixed-seed generator: `src/generate_data.py` (seed 20261029)
- Analysis pipeline: `src/analyze.py`
- Build orchestrator: `src/run_pipeline.py`
- SQL schema, seed data, business queries, and QA queries
- 7,200-row synthetic CSV and SQLite database in the downloadable package
- Excel workbook with formula-driven KPI and segment sheets plus three charts in the downloadable package
- Self-contained HTML dashboard, two PNG charts, findings, metric summary, and data dictionary
- Eleven automated unit tests and ten SQL-backed QA checks

## Verification
- Pipeline completed successfully on 2026-10-29.
- Unit tests: **11 passed, 0 failed**.
- QA checks: **10/10 passed**.
- SQL seed test: 120 appointment rows and six clinic dimension rows inserted successfully locally.
- All seven business queries executed against the seeded SQLite schema.
- Dashboard JavaScript passed `node --check`.
- Workbook inspected for formulas and charts; formulas are configured to recalculate when opened in Excel.
- Full and source ZIP packages passed integrity checks.

## Main computed results
- 7,200 appointment records; 1 April–27 September 2026.
- 5,600 attended, 696 no-show, 569 cancelled, 335 rescheduled.
- No-show rate: 11.05% using Attended + No-show as denominator.
- Cancellation rate: 7.90% using all scheduled records as denominator.
- Average booking lead time: 11.00 days.
- Average wait among attended records: 25.26 minutes.
- Reminder coverage: 82.07%.

## Interpretation limitations
Outcomes follow explicit probability rules, so segment patterns are partly encoded in the data. Reminder status is not randomized; group differences are not causal. This is an operations analytics demonstration, not a clinical or patient-level decision system.

## Repository and deployment
Verified public repository: `AbuHumzaKhan/AHK-Portfolio.github.io`. The project README, Python source, SQL schema/queries/seed sample, dashboard template/preview, metrics, QA results, data dictionary, deployment guide, changelog, license, and build audit were committed and fetched back through the GitHub connector. The portfolio `README.md` index was updated and fetched back for verification. A standalone repository was not created because the connected GitHub tool set has no repository-creation operation. The full CSV, SQLite database, Excel workbook, PNG charts, and generated full interactive dashboard were not individually committed: this connector workflow does not provide a local-file upload bridge, and large binary/base64 payloads are impractical to transfer through text arguments. They are included in the downloadable project ZIP. The repository includes source code and a static dashboard preview. No GitHub Pages deployment or hosted dashboard URL was verified; no live deployment is claimed.

The existing **Actual vs Budget — Executive Dashboard** project was not modified, refreshed, or appended to.
