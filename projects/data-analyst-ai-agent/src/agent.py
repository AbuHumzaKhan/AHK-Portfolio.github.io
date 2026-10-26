"""Context-aware local analytics agent using allow-listed SQL templates.

This deterministic prototype is not an LLM. The benchmark isolates how
business-context aliases improve intent routing while SQL templates keep
execution bounded and auditable.
"""
from __future__ import annotations
import argparse, json, re, sqlite3, statistics
from pathlib import Path
from typing import Any
ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "agent_demo.sqlite"
CONTEXT_PATH = ROOT / "context" / "business_context.json"

SQL = {
 "active_accounts": "SELECT COUNT(*) FROM accounts WHERE account_status='active'",
 "mrr": "SELECT COALESCE(ROUND(SUM(monthly_contract_value_inr),2),0) FROM accounts WHERE account_status='active'",
 "billed_revenue": "SELECT COALESCE(ROUND(SUM(amount_inr),2),0) FROM invoices WHERE invoice_status IN ('paid','open')",
 "paid_revenue": "SELECT COALESCE(ROUND(SUM(paid_amount_inr),2),0) FROM invoices WHERE invoice_status='paid'",
 "overdue_balance": "SELECT COALESCE(ROUND(SUM(amount_inr-paid_amount_inr),2),0) FROM invoices WHERE invoice_status='open' AND due_date < '2026-10-01'",
 "churned_accounts": "SELECT COUNT(*) FROM accounts WHERE account_status='churned'",
 "avg_mrr_active": "SELECT COALESCE(ROUND(AVG(monthly_contract_value_inr),2),0) FROM accounts WHERE account_status='active'",
 "mrr_by_plan": "SELECT plan_tier, ROUND(SUM(monthly_contract_value_inr),2) AS value FROM accounts WHERE account_status='active' GROUP BY plan_tier ORDER BY value DESC, plan_tier",
 "active_by_region": "SELECT region, COUNT(*) AS value FROM accounts WHERE account_status='active' GROUP BY region ORDER BY value DESC, region",
 "unresolved_tickets": "SELECT COUNT(*) FROM support_tickets WHERE status IN ('open','in_progress')",
 "unresolved_ticket_rate": "SELECT ROUND(100.0*SUM(CASE WHEN status IN ('open','in_progress') THEN 1 ELSE 0 END)/COUNT(*),2) FROM support_tickets",
 "median_resolution_hours": "SELECT AVG(resolution_hours) FROM support_tickets WHERE status='resolved' AND resolution_hours IS NOT NULL",
 "active_usage_accounts_sep": "SELECT COUNT(DISTINCT u.account_id) FROM usage_daily u JOIN accounts a USING(account_id) WHERE a.account_status='active' AND u.usage_date BETWEEN '2026-09-01' AND '2026-09-30' AND u.active_users>0",
 "api_calls_sep": "SELECT COALESCE(SUM(api_calls),0) FROM usage_daily WHERE usage_date BETWEEN '2026-09-01' AND '2026-09-30'",
 "billed_by_segment": "SELECT a.segment, ROUND(SUM(i.amount_inr),2) AS value FROM invoices i JOIN accounts a USING(account_id) WHERE i.invoice_status IN ('paid','open') GROUP BY a.segment ORDER BY value DESC, a.segment",
 "overdue_invoice_count": "SELECT COUNT(*) FROM invoices WHERE invoice_status='open' AND due_date < '2026-10-01'",
 "avg_high_priority_resolution": "SELECT COALESCE(ROUND(AVG(resolution_hours),2),0) FROM support_tickets WHERE priority='high' AND status='resolved'",
 "void_invoice_amount": "SELECT COALESCE(ROUND(SUM(amount_inr),2),0) FROM invoices WHERE invoice_status='void'",
 "trial_accounts": "SELECT COUNT(*) FROM accounts WHERE account_status='trial'",
 "churn_rate": "SELECT ROUND(100.0*SUM(CASE WHEN account_status='churned' THEN 1 ELSE 0 END)/COUNT(*),2) FROM accounts",
 "collection_rate": "SELECT ROUND(100.0*SUM(CASE WHEN invoice_status='paid' THEN paid_amount_inr ELSE 0 END)/SUM(CASE WHEN invoice_status IN ('paid','open') THEN amount_inr ELSE 0 END),2) FROM invoices",
 "tickets_by_segment": "SELECT a.segment, COUNT(*) AS value FROM support_tickets t JOIN accounts a USING(account_id) GROUP BY a.segment ORDER BY value DESC, a.segment",
 "sep_ticket_accounts": "SELECT COUNT(DISTINCT account_id) FROM support_tickets WHERE created_date BETWEEN '2026-09-01' AND '2026-09-30'",
 "active_seats": "SELECT COALESCE(SUM(seats_purchased),0) FROM accounts WHERE account_status='active'"
}

def load_context(path: Path = CONTEXT_PATH) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()

def route_question(question: str, mode: str = "full", context: dict[str, Any] | None = None) -> str | None:
    if mode not in {"baseline", "full"}:
        raise ValueError("mode must be 'baseline' or 'full'")
    context = context or load_context()
    q = f" {normalize(question)} "
    candidates: list[tuple[int, str, str]] = []
    for intent, spec in context["intents"].items():
        aliases = spec["baseline_aliases"] if mode == "baseline" else spec["aliases"]
        for alias in aliases:
            phrase = normalize(alias)
            if phrase and f" {phrase} " in q:
                candidates.append((len(phrase), intent, phrase))
    if not candidates:
        return None
    candidates.sort(key=lambda item: (item[0], item[1]), reverse=True)
    longest = candidates[0][0]
    winners = {intent for size, intent, _ in candidates if size == longest}
    return next(iter(winners)) if len(winners) == 1 else None

def execute_intent(intent: str, db_path: Path = DB_PATH) -> Any:
    if intent not in SQL:
        raise KeyError(f"Intent not allow-listed: {intent}")
    with sqlite3.connect(f"file:{db_path.resolve()}?mode=ro", uri=True) as con:
        if intent == "median_resolution_hours":
            vals = [r[0] for r in con.execute("SELECT resolution_hours FROM support_tickets WHERE status='resolved' AND resolution_hours IS NOT NULL ORDER BY resolution_hours")]
            return statistics.median(vals) if vals else None
        rows = con.execute(SQL[intent]).fetchall()
    if intent in {"mrr_by_plan", "active_by_region", "billed_by_segment", "tickets_by_segment"}:
        return rows
    return rows[0][0] if rows else None

def format_answer(value: Any) -> str:
    if value is None: return "NO DATA"
    if isinstance(value, list):
        parts = []
        for label, number in value:
            formatted = f"{float(number):.2f}" if isinstance(number, (float, int)) else str(number)
            parts.append(f"{label}={formatted}")
        return " | ".join(parts)
    if isinstance(value, bool): return str(value).lower()
    if isinstance(value, int): return str(value)
    if isinstance(value, float): return f"{value:.2f}"
    return str(value)

def answer_question(question: str, mode: str = "full", db_path: Path = DB_PATH) -> dict[str, Any]:
    intent = route_question(question, mode=mode)
    if intent is None:
        return {"question": question, "mode": mode, "intent": None, "answer": "UNANSWERED", "sql": None}
    value = execute_intent(intent, db_path)
    return {"question": question, "mode": mode, "intent": intent, "answer": format_answer(value), "sql": SQL.get(intent)}

def main() -> None:
    parser = argparse.ArgumentParser(description="Ask a supported business question of the synthetic SaaS dataset.")
    parser.add_argument("question", nargs="+", help="Business question in plain English")
    parser.add_argument("--mode", choices=["baseline", "full"], default="full")
    parser.add_argument("--db", type=Path, default=DB_PATH)
    args = parser.parse_args()
    result = answer_question(" ".join(args.question), args.mode, args.db)
    print(json.dumps(result, indent=2))

if __name__ == "__main__": main()
