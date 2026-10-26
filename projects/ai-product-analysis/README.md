# AI Product Analysis — User Interaction and Cost per Successful Output

**Build date:** 26 October 2026  
**Created by:** Abu Humza Khan

This project analyzes AI request outcomes, edits, regenerations, rejections, failures, latency, tokens, and modeled cost per successful output. The local build uses Python, SQLite, SQL, an offline HTML dashboard, and Power BI M/DAX build assets.

## Synthetic scenario results

| Metric | Result |
|---|---:|
| Requests | 3,000 |
| Interaction events | 9,123 |
| Accepted without edits | 1,352 |
| Edited then accepted | 921 |
| Rejected | 548 |
| Failed | 179 |
| Successful outputs (accepted + edited) | 2,273 (75.77%) |
| Regeneration rate | 48.43% |
| Rejection rate among completed requests | 19.43% |
| Failure rate | 5.97% |
| Total modeled generation cost | $22.898775 |
| Cost per successful output | $0.010074 |
| P95 total latency | 22,239 ms |
| QA checks | 11/11 passed |
| Automated tests | 12 passed |

All requests, outcomes, model tiers, and token-rate assumptions are synthetic. The fictional rates are scenario assumptions, not current vendor prices. No real prompts or user identifiers are included.

## Metric definitions

- Successful output: accepted or edited-then-accepted.
- Acceptance/edit/rejection rates use completed requests as the denominator.
- Failure rate uses all requests.
- Regeneration rate counts requests with at least one regeneration.
- Cost per successful output = total cost across all generation attempts / accepted-or-edited outputs.
- Regeneration-attempt cost is tracked from event-level generation costs.

## Public showcase assets

- Dashboard: reports/ai_product_dashboard.html
- Findings: outputs/INITIAL_FINDINGS.md
- SQL schema and business queries: sql/
- Power BI measures and transformations: powerbi/
- Deployment steps: docs/deployment_guide.md

The complete local build bundle also contains the generated CSVs, SQLite database, Python pipeline, tests, and supporting outputs. The showcase folder does not contain all binary/data assets.

**Native Power BI status:** No .pbix file was generated. Build and validate the report in Power BI Desktop using the supplied M, DAX, CSVs, and model guide before claiming a native report or service publication.

## Deployment status

No hosted deployment is claimed. The dashboard is a self-contained static HTML file; the Power BI assets are build instructions only.

## Credits

Created by: Abu Humza Khan  
GitHub profile: https://github.com/AbuHumzaKhan  
LinkedIn profile: https://www.linkedin.com/in/abu-humza-khan/  
Source: ChatGPT  
Design Idea: ChatGPT
