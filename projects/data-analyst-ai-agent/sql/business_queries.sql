-- MRR is active-account contract value, not billed revenue or cash.
SELECT COUNT(*) AS active_accounts FROM accounts WHERE account_status='active';
SELECT ROUND(SUM(monthly_contract_value_inr),2) AS mrr_inr FROM accounts WHERE account_status='active';
-- Billed revenue excludes void invoices.
SELECT ROUND(SUM(amount_inr),2) AS billed_inr FROM invoices WHERE invoice_status IN ('paid','open');
SELECT ROUND(SUM(paid_amount_inr),2) AS cash_collected_inr FROM invoices WHERE invoice_status='paid';
-- As-of date: 2026-10-01.
SELECT ROUND(SUM(amount_inr-paid_amount_inr),2) AS overdue_balance_inr
FROM invoices WHERE invoice_status='open' AND due_date<'2026-10-01';
SELECT COUNT(*) AS unresolved_tickets FROM support_tickets WHERE status IN ('open','in_progress');
SELECT ROUND(100.0*SUM(CASE WHEN status IN ('open','in_progress') THEN 1 ELSE 0 END)/COUNT(*),2) AS unresolved_ticket_rate_pct
FROM support_tickets;
SELECT COUNT(DISTINCT u.account_id) AS active_usage_accounts
FROM usage_daily u JOIN accounts a USING(account_id)
WHERE a.account_status='active' AND u.usage_date BETWEEN '2026-09-01' AND '2026-09-30' AND u.active_users>0;
SELECT ROUND(100.0*SUM(CASE WHEN account_status='churned' THEN 1 ELSE 0 END)/COUNT(*),2) AS churn_rate_pct FROM accounts;
SELECT ROUND(100.0*SUM(CASE WHEN invoice_status='paid' THEN paid_amount_inr ELSE 0 END)/
  SUM(CASE WHEN invoice_status IN ('paid','open') THEN amount_inr ELSE 0 END),2) AS collection_rate_pct FROM invoices;
