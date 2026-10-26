# Data Dictionary

All data is synthetic, generated with seed 20261026 for 1 July–30 September 2026.

## ai_requests
- request_id: unique request key.
- request_ts: UTC request timestamp.
- product_area: synthetic feature area.
- model_tier: fictional Small, Medium, or Large tier.
- user_segment: Free, Team, or Enterprise.
- prompt_version: synthetic version label.
- input_tokens_total / output_tokens_total: tokens across all generation attempts.
- total_tokens: input + output token reconciliation field.
- regeneration_count: retries after the initial attempt.
- edit_size_pct: simulated edit size, nonzero for edited outcomes.
- final_outcome: accepted, edited, rejected, or failed.
- request_status: completed or failed.
- total_latency_ms: simulated sum of generation-attempt latency.
- input_cost_usd / output_cost_usd / total_cost_usd: illustrative modeled costs.
- successful_output: 1 for accepted or edited; 0 for rejected or failed.
- was_regenerated: 1 if at least one regeneration occurred.

## interaction_events
- event_id: unique event key.
- request_id: foreign key to ai_requests.
- event_ts: UTC event timestamp.
- event_sequence: unique event order within a request.
- event_type: generated, regenerated, edited, accepted, rejected, or failed.
- event_cost_usd: generation attempt cost; user-action events cost zero.
- event_latency_ms: simulated attempt latency; user-action events are zero.

## Illustrative prices per million tokens
Small: $0.20 input / $0.80 output; Medium: $1.50 / $6.00; Large: $5.00 / $20.00. These are scenario assumptions, not vendor quotes.
