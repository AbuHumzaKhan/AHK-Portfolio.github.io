# Healthcare Appointment Access & No-show Analytics

**Created by Abu Humza Khan**  
**Build date:** 29 October 2026  
**Tools:** Python, pandas, SQLite/SQL, Excel, HTML/CSS/JavaScript  
**Dataset:** Fully synthetic; no real patient or provider records.

## Business problem

Outpatient operations teams need to understand where scheduled capacity is lost to no-shows, cancellations, and reschedules, while monitoring access indicators such as booking lead time and waiting time. A single network-wide rate can hide differences between clinics, specialties, weekdays, and booking horizons.

This project builds a reproducible analysis workflow for a synthetic outpatient network. It is a portfolio case study—not a clinical decision system and not an analysis of a real healthcare provider.

## Questions addressed

1. What share of scheduled appointment records end as no-shows?
2. How do no-show rates vary by clinic and specialty?
3. Is longer booking lead time associated with different no-show rates in the generated scenario?
4. How do reminder-marked records compare with records not marked as reminded?
5. How do wait time and attendance outcomes vary across operating segments?
6. Which measures should operations teams validate before changing scheduling policy?

## Dataset and provenance

The pipeline generates **7,200 synthetic appointment records** across six synthetic clinics and eight specialties, covering **1 April–27 September 2026**. The generator uses fixed seed `20261029`. No external dataset is used and no patient-identifiable information is included.

## KPI snapshot

| KPI | Result |
|---|---:|
| Scheduled appointment records | 7,200 |
| Attended | 5,600 |
| No-shows | 696 |
| Cancelled | 569 |
| Rescheduled | 335 |
| No-show rate | 11.05% |
| Cancellation rate | 7.90% |
| Average booking lead time | 11.00 days |
| Average wait among attended records | 25.26 minutes |
| Reminder coverage | 82.07% |

**Definitions:** No-show rate = No-show / (Attended + No-show); cancelled and rescheduled records are excluded from that denominator. Cancellation rate = Cancelled / all scheduled records.

## Initial findings

- Highest clinic no-show rate in the generated scenario: **Northside Medical Centre (12.62%)**.
- Highest specialty no-show rate: **Cardiology (12.42%)**.
- No-show rate among records not marked with a reminder was **14.88%**, compared with **10.22%** among records marked with a reminder. This is descriptive only: reminder assignment is not randomized, so this is not causal evidence.

## Recommendations

- Pilot confirmation and easy-reschedule workflows at clinics with above-network no-show rates.
- Test shorter booking horizons or wait-list backfilling where supported by real data.
- Monitor waiting time alongside attendance; a lower no-show rate does not automatically imply better access.
- Validate definitions and results on governed operational data before changing scheduling policy.

## Project files

- `src/generate_data.py` — fixed-seed synthetic data generator.
- `src/analyze.py` — KPI pipeline, summaries, chart generation, and findings.
- `src/build_project.py` — SQLite, Excel workbook, dashboard, and QA build.
- `src/run_pipeline.py` — one-command build.
- `sql/schema.sql`, `sql/seed_data.sql`, `sql/business_queries.sql`, `sql/qa_checks.sql`.
- `excel/Appointment_Access_NoShow_Analysis.xlsx` — formula-driven KPI workbook and charts (included in downloadable bundle; binary workbook not stored in this showcase).
- [`reports/dashboard_showcase.html`](reports/dashboard_showcase.html) — static dashboard preview for portfolio visitors.\n- `reports/dashboard.html` — full interactive report generated locally from `reports/dashboard_template.html` and summary data; the generated version is included in the downloadable bundle.
- `outputs/INITIAL_FINDINGS.md`, `outputs/metrics_summary.json`, `outputs/qa_checks.csv`.
- `docs/data_dictionary.md`, `docs/deployment_guide.md`, `CHANGELOG.md`, `BUILD_AUDIT.md`, `tests/test_pipeline.py`.\n\nThe public showcase includes a small SQL seed example. Running the pipeline regenerates the 120-row SQL sample, complete 7,200-row CSV, SQLite database, Excel workbook, full interactive dashboard, charts, and QA artefacts. The generated CSV, database, workbook, and full interactive dashboard are in the downloadable package rather than individually committed here.

## Run locally

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/run_pipeline.py
python -m unittest discover -s tests -v
```

Then open `reports/dashboard.html` in a browser and `excel/Appointment_Access_NoShow_Analysis.xlsx` in Excel. See `docs/deployment_guide.md` for full setup and publishing instructions.

## Limitations

- Outcomes are simulated with explicit probability rules, so some segment patterns are partly built into the generator.
- Reminder status is not randomized. Group differences are not causal.
- Records are appointment instances, not longitudinal patient journeys.
- No clinical decisions, individual patient risk scores, or monetary savings estimates are produced.
- This project does not include a native Power BI `.pbix`; it uses Python, SQL, Excel, and a local HTML dashboard.
- The checked-in SQL seed is a lightweight example; the pipeline regenerates a 120-row sample. The full 7,200-row dataset is reproducibly generated from source code.

## Change log

Initial portfolio release — 2026-10-29. See `CHANGELOG.md` for details.

## Credits

Created by: Abu Humza Khan  
GitHub profile: https://github.com/AbuHumzaKhan  
LinkedIn profile: https://www.linkedin.com/in/abu-humza-khan/  
Source: ChatGPT  
Design Idea: ChatGPT
