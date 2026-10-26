"""Run compact QA checks over the synthetic CSVs and SQLite database."""
from pathlib import Path
import sqlite3
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def run():
    d=ROOT/"data"; a=pd.read_csv(d/"accounts.csv"); i=pd.read_csv(d/"invoices.csv"); u=pd.read_csv(d/"usage_daily.csv"); t=pd.read_csv(d/"support_tickets.csv")
    ids=set(a.account_id)
    checks=[
      ("accounts_pk_unique",a.account_id.is_unique),
      ("invoices_pk_unique",i.invoice_id.is_unique),
      ("usage_composite_key_unique",not u.duplicated(["usage_date","account_id"]).any()),
      ("tickets_pk_unique",t.ticket_id.is_unique),
      ("invoice_fk_coverage",i.account_id.isin(ids).all()),
      ("usage_fk_coverage",u.account_id.isin(ids).all()),
      ("ticket_fk_coverage",t.account_id.isin(ids).all()),
      ("nonnegative_financials",i[["amount_inr","paid_amount_inr"]].ge(0).all().all()),
      ("nonnegative_usage",u[["active_users","sessions","api_calls"]].ge(0).all().all()),
      ("resolved_hours_consistency",t.loc[t.status.eq("resolved"),"resolution_hours"].notna().all() and t.loc[~t.status.eq("resolved"),"resolution_hours"].isna().all())
    ]
    with sqlite3.connect(d/"agent_demo.sqlite") as con: checks.append(("sqlite_foreign_keys",len(con.execute("PRAGMA foreign_key_check").fetchall())==0))
    out=pd.DataFrame([{"check":name,"passed":bool(ok)} for name,ok in checks]); out.to_csv(ROOT/"outputs"/"qa_checks.csv",index=False)
    if not out.passed.all(): raise SystemExit("QA failed")
    print(f"{int(out.passed.sum())}/{len(out)} checks passed")
if __name__=="__main__": run()
