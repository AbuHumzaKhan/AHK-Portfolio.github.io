-- Rates are computed from totals, not averages of row-level rates.

-- 1. Executive KPI summary
SELECT COUNT(*) AS campaign_days, SUM(impressions) AS impressions, SUM(clicks) AS clicks,
       ROUND(1.0*SUM(clicks)/NULLIF(SUM(impressions),0),4) AS ctr,
       ROUND(SUM(spend_usd),2) AS spend_usd, SUM(conversions) AS conversions,
       ROUND(1.0*SUM(spend_usd)/NULLIF(SUM(conversions),0),2) AS cpa_usd,
       ROUND(SUM(revenue_usd),2) AS revenue_usd,
       ROUND(1.0*SUM(revenue_usd)/NULLIF(SUM(spend_usd),0),2) AS roas
FROM campaign_daily_performance;

-- 2. Channel efficiency ranking
SELECT c.channel, SUM(d.impressions) AS impressions, SUM(d.clicks) AS clicks,
       ROUND(1.0*SUM(d.clicks)/NULLIF(SUM(d.impressions),0),4) AS ctr,
       ROUND(SUM(d.spend_usd),2) AS spend_usd, SUM(d.conversions) AS conversions,
       ROUND(1.0*SUM(d.spend_usd)/NULLIF(SUM(d.conversions),0),2) AS cpa_usd,
       ROUND(SUM(d.revenue_usd),2) AS revenue_usd,
       ROUND(1.0*SUM(d.revenue_usd)/NULLIF(SUM(d.spend_usd),0),2) AS roas
FROM campaign_daily_performance d JOIN campaigns c USING(campaign_id)
GROUP BY c.channel ORDER BY roas DESC;

-- 3. Campaign scorecard
SELECT c.campaign_id,c.campaign_name,c.channel, SUM(d.clicks) clicks, SUM(d.conversions) conversions,
       ROUND(SUM(d.spend_usd),2) spend_usd, ROUND(SUM(d.revenue_usd),2) revenue_usd,
       ROUND(1.0*SUM(d.spend_usd)/NULLIF(SUM(d.conversions),0),2) cpa_usd,
       ROUND(1.0*SUM(d.revenue_usd)/NULLIF(SUM(d.spend_usd),0),2) roas
FROM campaign_daily_performance d JOIN campaigns c USING(campaign_id)
GROUP BY c.campaign_id,c.campaign_name,c.channel ORDER BY roas DESC;

-- 4. Weekly trend
SELECT strftime('%Y-%W',date) AS year_week, ROUND(SUM(spend_usd),2) spend_usd,
       SUM(conversions) conversions, ROUND(SUM(revenue_usd),2) revenue_usd,
       ROUND(1.0*SUM(revenue_usd)/NULLIF(SUM(spend_usd),0),2) roas
FROM campaign_daily_performance GROUP BY year_week ORDER BY year_week;

-- 5. High-spend campaigns below portfolio ROAS (diagnostic only)
WITH total AS (SELECT 1.0*SUM(revenue_usd)/NULLIF(SUM(spend_usd),0) portfolio_roas FROM campaign_daily_performance),
by_campaign AS (
  SELECT c.campaign_name,c.channel,SUM(d.spend_usd) spend_usd,
         1.0*SUM(d.revenue_usd)/NULLIF(SUM(d.spend_usd),0) roas
  FROM campaign_daily_performance d JOIN campaigns c USING(campaign_id)
  GROUP BY c.campaign_id,c.campaign_name,c.channel
)
SELECT b.*,ROUND(t.portfolio_roas,2) portfolio_roas
FROM by_campaign b CROSS JOIN total t
WHERE b.spend_usd >= (SELECT AVG(spend_usd) FROM by_campaign) AND b.roas < t.portfolio_roas
ORDER BY b.spend_usd DESC;