# Power BI Model and Report Guide

1. Create a text parameter named ProjectRoot pointing to the project's data folder.
2. Create CampaignDaily from PowerQuery_M.pq and Campaigns from Campaigns_PowerQuery_M.pq.
3. Relate Campaigns[campaign_id] (one) to CampaignDaily[campaign_id] (many), single direction.
4. Create a Calendar table and relate Calendar[Date] to CampaignDaily[date].
5. Add measures from DAX_Measures.dax. Format CTR and Conversion Rate as percentages, currency measures as USD, and ROAS with an x suffix.

## Suggested pages

- Executive overview: Spend, Attributed Value, Conversions, CPA, ROAS, weekly trend, and channel ROAS.
- Campaign scorecard: spend, clicks, conversions, CPA, ROAS, and budget utilization.
- Channel and audience: channel/audience slicers and spend-versus-ROAS comparison.

## Validation

Reconcile spend, impressions, clicks, conversions, and attributed value to outputs/metrics_summary.json. Calculate rates from totals rather than averaging daily rates. Review zero-conversion campaigns so CPA displays blank rather than infinity.

**Native .pbix status:** not generated. DAX, M, model instructions, and HTML/SVG previews are implementation assets only.