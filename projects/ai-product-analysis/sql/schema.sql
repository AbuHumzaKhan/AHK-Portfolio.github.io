PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS interaction_events;
DROP TABLE IF EXISTS ai_requests;
CREATE TABLE ai_requests (
 request_id TEXT PRIMARY KEY, request_ts TEXT NOT NULL, product_area TEXT NOT NULL,
 model_tier TEXT NOT NULL CHECK(model_tier IN ('Small','Medium','Large')), user_segment TEXT NOT NULL,
 prompt_version TEXT NOT NULL, input_tokens_total INTEGER NOT NULL CHECK(input_tokens_total>=0),
 output_tokens_total INTEGER NOT NULL CHECK(output_tokens_total>=0), total_tokens INTEGER NOT NULL CHECK(total_tokens>=0),
 regeneration_count INTEGER NOT NULL CHECK(regeneration_count>=0), edit_size_pct REAL NOT NULL CHECK(edit_size_pct BETWEEN 0 AND 100),
 final_outcome TEXT NOT NULL CHECK(final_outcome IN ('accepted','edited','rejected','failed')),
 request_status TEXT NOT NULL CHECK(request_status IN ('completed','failed')), total_latency_ms INTEGER NOT NULL CHECK(total_latency_ms>=0),
 input_cost_usd REAL NOT NULL CHECK(input_cost_usd>=0), output_cost_usd REAL NOT NULL CHECK(output_cost_usd>=0),
 total_cost_usd REAL NOT NULL CHECK(total_cost_usd>=0), successful_output INTEGER NOT NULL CHECK(successful_output IN (0,1)),
 was_regenerated INTEGER NOT NULL CHECK(was_regenerated IN (0,1))
);
CREATE TABLE interaction_events (
 event_id TEXT PRIMARY KEY, request_id TEXT NOT NULL REFERENCES ai_requests(request_id),
 event_ts TEXT NOT NULL, event_sequence INTEGER NOT NULL CHECK(event_sequence>0),
 event_type TEXT NOT NULL CHECK(event_type IN ('generated','regenerated','edited','accepted','rejected','failed')),
 model_tier TEXT NOT NULL, event_cost_usd REAL NOT NULL CHECK(event_cost_usd>=0),
 event_latency_ms INTEGER NOT NULL CHECK(event_latency_ms>=0), UNIQUE(request_id,event_sequence)
);
CREATE INDEX idx_requests_ts ON ai_requests(request_ts);
CREATE INDEX idx_requests_area_outcome ON ai_requests(product_area,final_outcome);
CREATE INDEX idx_events_request_type ON interaction_events(request_id,event_type);
