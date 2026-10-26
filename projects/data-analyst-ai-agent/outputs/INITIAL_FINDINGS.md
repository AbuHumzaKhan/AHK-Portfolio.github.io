# Initial Findings — Data Analyst AI Agent

**Date:** 26 October 2026  
**Provenance:** Synthetic B2B SaaS data, seed 20261026; as-of date 1 October 2026.

## Context benchmark

- Baseline: 8 of 24 known-answer questions correct (33.33%).
- Full business context: 24 of 24 correct (100.00%).
- Difference: +66.67 percentage points.
- Unanswered questions: 16 before context; 0 after context.

This result measures a deterministic phrase router selecting from allow-listed SQL templates. The test set is curated and not an independent holdout. Do not present this as general LLM accuracy.

## Scenario metrics

- Active accounts: 92; trial accounts: 8; churned accounts: 20.
- Active-account MRR: ₹546,906.59.
- Billed revenue excluding void invoices: ₹4,139,295.18.
- Cash collected on paid invoices: ₹3,368,926.64.
- Overdue receivables at 1 October 2026: ₹770,368.54 across 119 invoices.
- Collection rate under the documented definition: 81.39%.
- Unresolved support tickets: 91 (25.28%).

## Recommendations

1. Obtain stakeholder sign-off on MRR, billed revenue, collections, churn, and overdue-balance definitions.
2. Test on a separate holdout set containing ambiguous and unsupported questions.
3. Log the matched intent, SQL template, source rows, and execution status for every answer.
4. Require clarification or abstention when multiple definitions may apply.
5. Add authentication, tenant isolation, audit logging, and rate limits before exposing an API publicly.

All amounts and records are synthetic; no real company is represented.
