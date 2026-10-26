-- Marketing Campaign Performance & Budget Efficiency Analytics
-- SQLite-compatible schema; synthetic scenario, illustrative USD values.
PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS campaign_daily_performance;
DROP TABLE IF EXISTS campaigns;
CREATE TABLE campaigns (
    campaign_id TEXT PRIMARY KEY,
    campaign_name TEXT NOT NULL UNIQUE,
    channel TEXT NOT NULL,
    objective TEXT NOT NULL,
    audience_segment TEXT NOT NULL,
    daily_budget_usd REAL NOT NULL CHECK (daily_budget_usd >= 0)
);
CREATE TABLE campaign_daily_performance (
    date TEXT NOT NULL,
    campaign_id TEXT NOT NULL,
    impressions INTEGER NOT NULL CHECK (impressions >= 0),
    clicks INTEGER NOT NULL CHECK (clicks >= 0 AND clicks <= impressions),
    spend_usd REAL NOT NULL CHECK (spend_usd >= 0),
    conversions INTEGER NOT NULL CHECK (conversions >= 0),
    revenue_usd REAL NOT NULL CHECK (revenue_usd >= 0),
    PRIMARY KEY (date, campaign_id),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(campaign_id)
);
CREATE INDEX idx_campaign_daily_date ON campaign_daily_performance(date);
CREATE INDEX idx_campaign_daily_campaign ON campaign_daily_performance(campaign_id);