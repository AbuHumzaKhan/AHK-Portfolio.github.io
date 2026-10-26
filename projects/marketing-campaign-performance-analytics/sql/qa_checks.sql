-- Each query should return zero failures.
SELECT 'row_count_expected_672' check_name, CASE WHEN COUNT(*)=672 THEN 0 ELSE 1 END failures FROM campaign_daily_performance;
SELECT 'unique_campaign_day' check_name, CASE WHEN COUNT(*)=COUNT(DISTINCT date || '|' || campaign_id) THEN 0 ELSE 1 END failures FROM campaign_daily_performance;
SELECT 'nonnegative_metrics' check_name, COUNT(*) failures FROM campaign_daily_performance WHERE impressions<0 OR clicks<0 OR clicks>impressions OR spend_usd<0 OR conversions<0 OR revenue_usd<0;
SELECT 'orphan_campaigns' check_name, COUNT(*) failures FROM campaign_daily_performance d LEFT JOIN campaigns c USING(campaign_id) WHERE c.campaign_id IS NULL;
SELECT 'date_range' check_name, CASE WHEN MIN(date)='2026-07-06' AND MAX(date)='2026-09-27' THEN 0 ELSE 1 END failures FROM campaign_daily_performance;
SELECT 'campaign_count_expected_8' check_name, CASE WHEN COUNT(*)=8 THEN 0 ELSE 1 END failures FROM campaigns;