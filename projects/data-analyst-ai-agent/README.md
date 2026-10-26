# Data Analyst AI Agent — Context-Aware Business Question Answering

**Build date:** 26 October 2026  
**Created by:** Abu Humza Khan

A local-first analytics-agent prototype that tests how table descriptions, metric definitions, business rules, and domain vocabulary affect the accuracy of business-question routing. The full local build uses Python, SQLite, allow-listed SQL templates, a FastAPI demo, a 24-question benchmark, an Excel workbook, and an offline HTML report.

## Benchmark result

| Metric | Result |
|---|---:|
| Known-answer questions | 24 |
| Baseline exact-answer accuracy | 33.33% (8/24) |
| Full-context exact-answer accuracy | 100.00% (24/24) |
| Improvement on this curated test set | +66.67 percentage points |
| Data QA checks | 11/11 passed |
| Automated tests | 14 passed |

**Interpretation:** This is a deterministic phrase-router/context ablation, not a general LLM benchmark. The questions, aliases, and SQL templates were authored together. The 100% result applies only to this curated test set and does not demonstrate broad language understanding.

## Synthetic data

The fictional B2B SaaS scenario contains 120 accounts, 720 invoices, 11,040 daily usage rows, and 360 support tickets. All records are generated with seed 20261026. No real customer data is used.

Selected scenario metrics: 92 active accounts; active-account MRR ₹546,906.59; billed revenue excluding void invoices ₹4,139,295.18; cash collected ₹3,368,926.64; overdue receivables ₹770,368.54; 91 unresolved tickets.

## Business rules demonstrated

- MRR is the contracted monthly value of active accounts, not invoice revenue or cash collected.
- Billed revenue includes paid and open invoices, excluding void invoices.
- Cash collected includes paid invoices only.
- Overdue receivables are open invoices due before 1 October 2026.
- Unresolved support cases have status open or in_progress.

## Assets in this portfolio showcase

- Dashboard: reports/context_accuracy_dashboard.html
- Findings: outputs/INITIAL_FINDINGS.md
- SQL schema and business queries: sql/
- Business context and definitions: context/business_context.json
- Deployment steps: docs/deployment_guide.md

The complete local build bundle also contains the generated CSVs, SQLite database, Python pipeline, test suite, and Excel workbook. The showcase folder does not contain all binary/data assets.

## Deployment status

The local FastAPI smoke test passed. No hosted API or website deployment is claimed. The public portfolio folder is a showcase, not a standalone repository. Repository creation is not available through the connected GitHub toolset.

## Credits

Created by: Abu Humza Khan  
GitHub profile: https://github.com/AbuHumzaKhan  
LinkedIn profile: https://www.linkedin.com/in/abu-humza-khan/  
Source: ChatGPT  
Design Idea: ChatGPT
