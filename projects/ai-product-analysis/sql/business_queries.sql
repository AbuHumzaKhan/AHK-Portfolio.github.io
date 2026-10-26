-- Successful output = accepted OR edited-then-accepted.
SELECT COUNT(*) AS total_requests FROM ai_requests;
SELECT final_outcome, COUNT(*) AS requests FROM ai_requests GROUP BY final_outcome;
SELECT SUM(successful_output) AS successful_outputs,
 ROUND(SUM(total_cost_usd)/NULLIF(SUM(successful_output),0),6) AS cost_per_successful_output_usd
FROM ai_requests;
SELECT ROUND(100.0*SUM(was_regenerated)/COUNT(*),2) AS regeneration_rate_pct FROM ai_requests;
SELECT product_area, COUNT(*) AS requests, SUM(successful_output) AS successful_outputs,
 ROUND(SUM(total_cost_usd),6) AS total_cost_usd,
 ROUND(SUM(total_cost_usd)/NULLIF(SUM(successful_output),0),6) AS cost_per_successful_output_usd
FROM ai_requests GROUP BY product_area ORDER BY total_cost_usd DESC;
SELECT model_tier, COUNT(*) AS requests,
 ROUND(100.0*SUM(successful_output)/COUNT(*),2) AS successful_output_rate_pct,
 ROUND(SUM(total_cost_usd)/NULLIF(SUM(successful_output),0),6) AS cost_per_successful_output_usd
FROM ai_requests GROUP BY model_tier;
SELECT event_type, COUNT(*) AS event_count, ROUND(SUM(event_cost_usd),6) AS event_cost_usd
FROM interaction_events GROUP BY event_type;
SELECT ROUND((SELECT SUM(total_cost_usd) FROM ai_requests),8) AS request_cost,
 ROUND((SELECT SUM(event_cost_usd) FROM interaction_events),8) AS event_cost;
