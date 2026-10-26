PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS support_tickets;
DROP TABLE IF EXISTS usage_daily;
DROP TABLE IF EXISTS invoices;
DROP TABLE IF EXISTS accounts;
CREATE TABLE accounts (
  account_id TEXT PRIMARY KEY, account_name TEXT NOT NULL, segment TEXT NOT NULL,
  region TEXT NOT NULL, plan_tier TEXT NOT NULL,
  account_status TEXT NOT NULL CHECK(account_status IN ('active','trial','churned')),
  seats_purchased INTEGER NOT NULL CHECK(seats_purchased >= 0), start_date TEXT NOT NULL,
  monthly_contract_value_inr REAL NOT NULL CHECK(monthly_contract_value_inr >= 0), account_manager TEXT NOT NULL
);
CREATE TABLE invoices (
  invoice_id TEXT PRIMARY KEY, account_id TEXT NOT NULL REFERENCES accounts(account_id),
  invoice_date TEXT NOT NULL, due_date TEXT NOT NULL,
  invoice_status TEXT NOT NULL CHECK(invoice_status IN ('paid','open','void')),
  amount_inr REAL NOT NULL CHECK(amount_inr >= 0), paid_amount_inr REAL NOT NULL CHECK(paid_amount_inr >= 0)
);
CREATE TABLE usage_daily (
  usage_date TEXT NOT NULL, account_id TEXT NOT NULL REFERENCES accounts(account_id),
  active_users INTEGER NOT NULL CHECK(active_users >= 0), sessions INTEGER NOT NULL CHECK(sessions >= 0),
  api_calls INTEGER NOT NULL CHECK(api_calls >= 0), PRIMARY KEY(usage_date, account_id)
);
CREATE TABLE support_tickets (
  ticket_id TEXT PRIMARY KEY, account_id TEXT NOT NULL REFERENCES accounts(account_id),
  created_date TEXT NOT NULL, resolved_date TEXT, priority TEXT NOT NULL CHECK(priority IN ('low','medium','high')),
  status TEXT NOT NULL CHECK(status IN ('resolved','open','in_progress')), category TEXT NOT NULL, resolution_hours REAL
);
CREATE INDEX idx_invoices_status_due ON invoices(invoice_status, due_date);
CREATE INDEX idx_usage_date ON usage_daily(usage_date);
CREATE INDEX idx_tickets_created_status ON support_tickets(created_date, status);
