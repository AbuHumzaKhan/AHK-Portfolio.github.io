# Data Dictionary

**Provenance:** generated deterministically for this portfolio project with Python standard-library random seed 20261026 on 26 October 2026. No real advertiser or customer records are included. All currency values are illustrative USD.

## campaigns table / campaigns.csv

| Field | Type | Definition |
|---|---|---|
| campaign_id | text | Stable synthetic campaign key; primary key. |
| campaign_name | text | Campaign display name. |
| channel | text | Paid media or lifecycle channel grouping. |
| objective | text | Intended campaign objective. |
| audience_segment | text | Synthetic audience grouping. |
| daily_budget_usd | decimal | Illustrative planned daily budget. |

## campaign_daily_performance table / campaign_daily_performance.csv

| Field | Type | Definition |
|---|---|---|
| date | ISO date | Reporting date, 2026-07-06 through 2026-09-27. |
| campaign_id | text | Foreign key to campaigns. |
| campaign_name | text | Denormalized display label for Excel/Power BI convenience. |
| channel | text | Denormalized channel label. |
| objective | text | Campaign objective. |
| audience_segment | text | Synthetic target audience. |
| impressions | integer | Simulated ad/email impression proxy. |
| clicks | integer | Simulated clicks; never greater than impressions. |
| spend_usd | decimal | Simulated media/platform cost plus a small daily overhead. |
| conversions | integer | Simulated attributed purchase conversions. |
| revenue_usd | decimal | Simulated attributed conversion value, not audited net revenue. |
| daily_budget_usd | decimal | Planned daily budget repeated in the export for utilization analysis. |

## KPI definitions

- CTR = total clicks / total impressions.
- CPC = total spend / total clicks.
- Conversion rate = total conversions / total clicks.
- CPA = total spend / total conversions.
- ROAS = total attributed value / total spend.
- Budget utilization = total spend / sum of daily budget values.

Calculate rates from summed numerators and denominators; do not average daily rates for portfolio or channel reporting.