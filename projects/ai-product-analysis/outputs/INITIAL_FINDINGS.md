# Initial Findings — AI Product Analysis

**Date range:** 1 July–30 September 2026  
**Provenance:** Synthetic deterministic telemetry; seed 20261026; illustrative token rates.

## Headline metrics

- Requests: 3,000; completed: 2,821.
- Accepted: 1,352; edited then accepted: 921; rejected: 548; failed: 179.
- Successful outputs under the project definition: 2,273 (75.77% of all requests).
- Total modeled generation cost: $22.898775.
- Cost per successful output: $0.010074.
- Regeneration rate: 48.43%; rejection rate among completed requests: 19.43%; failure rate: 5.97%.
- P95 total latency: 22,239 ms.
- Regeneration attempts account for 44.38% of modeled generation cost.

## Segment observations

- Code Assistant has the highest total modeled spend by product area in this run, but total spend is not evidence of waste because volume and task complexity differ.
- Large model tier has the highest cost per successful output and a higher synthetic success rate. This is a quality/cost trade-off, not a model recommendation.
- Regeneration is common in this scenario; examine task type, edit size, acceptance, and latency together before changing product defaults.

## Recommendations

1. Instrument the full lifecycle: generated, regenerated, edited, accepted, rejected, and failed.
2. Include every attempt's token cost, not just the final output.
3. Compare cost per successful output with acceptance, edit size, rejection, failure, and latency.
4. Run controlled routing experiments with task difficulty and user segment held constant.
5. Validate all definitions and prices against real telemetry before making decisions.

All records and prices are simulated. No causal claims are supported.
