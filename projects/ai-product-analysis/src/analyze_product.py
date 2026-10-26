"""Recompute core AI product metrics from the synthetic CSVs."""
from pathlib import Path
import json, sqlite3
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]

def analyze():
    data=ROOT/"data"; out=ROOT/"outputs"; out.mkdir(exist_ok=True)
    r=pd.read_csv(data/"ai_requests.csv"); e=pd.read_csv(data/"interaction_events.csv")
    total=len(r); completed=r.request_status.eq("completed"); successful=r.successful_output.eq(1)
    accepted=r.final_outcome.eq("accepted"); edited=r.final_outcome.eq("edited"); rejected=r.final_outcome.eq("rejected"); failed=r.final_outcome.eq("failed")
    total_cost=float(r.total_cost_usd.sum()); successful_count=int(successful.sum())
    regen_cost=float(e.loc[e.event_type.eq("regenerated"),"event_cost_usd"].sum())
    metrics={
      "total_requests":int(total),"completed_requests":int(completed.sum()),
      "accepted_requests":int(accepted.sum()),"edited_requests":int(edited.sum()),
      "rejected_requests":int(rejected.sum()),"failed_requests":int(failed.sum()),
      "successful_outputs":successful_count,"successful_output_rate_pct":round(100*successful_count/total,2),
      "acceptance_rate_pct_completed":round(100*accepted.sum()/max(1,completed.sum()),2),
      "edit_rate_pct_completed":round(100*edited.sum()/max(1,completed.sum()),2),
      "rejection_rate_pct_completed":round(100*rejected.sum()/max(1,completed.sum()),2),
      "failure_rate_pct_all":round(100*failed.sum()/total,2),
      "regeneration_rate_pct_all":round(100*r.was_regenerated.sum()/total,2),
      "requests_with_regeneration":int(r.was_regenerated.sum()),
      "total_cost_usd":round(total_cost,6),
      "cost_per_successful_output_usd":round(total_cost/max(1,successful_count),6),
      "average_cost_per_request_usd":round(total_cost/total,6),
      "total_tokens":int(r.total_tokens.sum()),"average_latency_ms":round(float(r.total_latency_ms.mean()),1),
      "p95_latency_ms":round(float(r.total_latency_ms.quantile(.95)),1),
      "average_edit_size_pct_edited_only":round(float(r.loc[edited,"edit_size_pct"].mean()),2),
      "regeneration_attempt_cost_share_pct":round(100*regen_cost/max(total_cost,1e-12),2),
      "dataset_provenance":"Synthetic deterministic telemetry; seed 20261026; illustrative pricing assumptions; no real product/user telemetry."
    }
    (out/"metrics_summary.json").write_text(json.dumps(metrics,indent=2),encoding="utf-8")
    checks=[
      ("request_pk_unique",r.request_id.is_unique),
      ("event_pk_unique",e.event_id.is_unique),
      ("event_fk_valid",e.request_id.isin(r.request_id).all()),
      ("success_flag_consistent",r.successful_output.eq(r.final_outcome.isin(["accepted","edited"]).astype(int)).all()),
      ("tokens_reconcile",r.total_tokens.eq(r.input_tokens_total+r.output_tokens_total).all()),
      ("request_event_cost_reconcile",abs(r.total_cost_usd.sum()-e.event_cost_usd.sum())<.0001),
      ("regeneration_events_reconcile",e.query("event_type == 'regenerated'").groupby("request_id").size().reindex(r.set_index("request_id").index,fill_value=0).eq(r.set_index("request_id").regeneration_count).all())
    ]
    pd.DataFrame([{"check":n,"passed":bool(ok)} for n,ok in checks]).to_csv(out/"qa_checks_core.csv",index=False)
    print(json.dumps(metrics,indent=2))
    return metrics
if __name__=="__main__": analyze()
