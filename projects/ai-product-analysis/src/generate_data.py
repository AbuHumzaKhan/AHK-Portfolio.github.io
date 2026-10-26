"""Generate deterministic synthetic AI-product request and interaction telemetry."""
from __future__ import annotations
import argparse, random
from datetime import datetime, timedelta, timezone
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
SEED=20261026
INPUT_RATE_PER_MILLION={"Small":0.20,"Medium":1.50,"Large":5.00}
OUTPUT_RATE_PER_MILLION={"Small":0.80,"Medium":6.00,"Large":20.00}
AREAS=["Writing Assistant","Code Assistant","Document Summary","Data Insights","Customer Support"]
SEGMENTS=["Free","Team","Enterprise"]
MODELS=["Small","Medium","Large"]

def generate(out_dir: Path=ROOT/"data", seed:int=SEED, n_requests:int=3000):
    rng=random.Random(seed); out_dir.mkdir(parents=True,exist_ok=True)
    requests=[]; events=[]; start=datetime(2026,7,1,tzinfo=timezone.utc); end=datetime(2026,10,1,tzinfo=timezone.utc)
    seconds=int((end-start).total_seconds())
    for i in range(1,n_requests+1):
        ts=start+timedelta(seconds=rng.randint(0,seconds-1))
        area=rng.choices(AREAS,weights=[0.25,0.22,0.18,0.18,0.17])[0]
        segment=rng.choices(SEGMENTS,weights=[0.48,0.36,0.16])[0]
        model=rng.choices(MODELS,weights=[0.46,0.38,0.16])[0]
        base_prompt=max(80,int(rng.lognormvariate(6.35,0.62)))
        base_output=max(40,int(rng.lognormvariate(6.05,0.70)))
        regen_count=rng.choices([0,1,2,3],weights=[0.58,0.25,0.12,0.05])[0]
        if area in {"Code Assistant","Data Insights"} and rng.random()<0.28: regen_count=min(3,regen_count+1)
        if segment=="Enterprise" and rng.random()<0.12: regen_count=max(0,regen_count-1)
        accepted_p={"Small":0.39,"Medium":0.47,"Large":0.53}[model]
        edited_p={"Small":0.31,"Medium":0.30,"Large":0.27}[model]
        rejected_p={"Small":0.22,"Medium":0.17,"Large":0.15}[model]
        failed_p=max(0.04,1-accepted_p-edited_p-rejected_p)
        if area=="Code Assistant": accepted_p-=0.04; edited_p+=0.06; rejected_p-=0.01; failed_p-=0.01
        if area=="Customer Support": accepted_p+=0.04; edited_p-=0.02; rejected_p-=0.01; failed_p-=0.01
        if segment=="Enterprise": accepted_p+=0.025; rejected_p-=0.015; edited_p-=0.01
        outcome=rng.choices(["accepted","edited","rejected","failed"],weights=[accepted_p,edited_p,rejected_p,failed_p])[0]
        attempts=[]
        for attempt in range(regen_count+1):
            input_tokens=max(30,int(base_prompt*rng.uniform(0.82,1.22)*(1.12 if attempt else 1.0)))
            output_tokens=max(20,int(base_output*rng.uniform(0.72,1.32)))
            model_factor={"Small":0.65,"Medium":1.0,"Large":1.55}[model]
            latency=max(120,int((input_tokens+output_tokens)*model_factor*rng.uniform(2.0,5.2)+rng.randint(80,400)))
            input_cost=input_tokens*INPUT_RATE_PER_MILLION[model]/1_000_000
            output_cost=output_tokens*OUTPUT_RATE_PER_MILLION[model]/1_000_000
            attempts.append({"input_tokens":input_tokens,"output_tokens":output_tokens,"latency_ms":latency,
                             "input_cost_usd":input_cost,"output_cost_usd":output_cost,"cost_usd":input_cost+output_cost})
        total_input=sum(x["input_tokens"] for x in attempts); total_output=sum(x["output_tokens"] for x in attempts)
        total_latency=sum(x["latency_ms"] for x in attempts); total_cost=sum(x["cost_usd"] for x in attempts)
        edit_pct=round(rng.uniform(2.5,58.0),2) if outcome=="edited" else 0.0
        request_id=f"REQ{i:05d}"
        requests.append({"request_id":request_id,"request_ts":ts.isoformat(),"product_area":area,"model_tier":model,
          "user_segment":segment,"prompt_version":rng.choice(["v1","v2","v3"]),
          "input_tokens_total":total_input,"output_tokens_total":total_output,"total_tokens":total_input+total_output,
          "regeneration_count":regen_count,"edit_size_pct":edit_pct,"final_outcome":outcome,
          "request_status":"failed" if outcome=="failed" else "completed","total_latency_ms":total_latency,
          "input_cost_usd":round(sum(x["input_cost_usd"] for x in attempts),8),
          "output_cost_usd":round(sum(x["output_cost_usd"] for x in attempts),8),
          "total_cost_usd":round(total_cost,8),"successful_output":int(outcome in {"accepted","edited"}),
          "was_regenerated":int(regen_count>0)})
        ev_seq=1; event_time=ts
        for attempt, detail in enumerate(attempts):
            if attempt>0: event_time+=timedelta(milliseconds=attempts[attempt-1]["latency_ms"])
            event_type="generated" if attempt==0 else "regenerated"
            events.append({"event_id":f"EV{i:05d}_{ev_seq:02d}","request_id":request_id,"event_ts":event_time.isoformat(),
              "event_sequence":ev_seq,"event_type":event_type,"model_tier":model,
              "event_cost_usd":round(detail["cost_usd"],8),"event_latency_ms":detail["latency_ms"]})
            ev_seq+=1
        event_time+=timedelta(milliseconds=attempts[-1]["latency_ms"])
        if outcome=="edited":
            events.append({"event_id":f"EV{i:05d}_{ev_seq:02d}","request_id":request_id,"event_ts":event_time.isoformat(),
              "event_sequence":ev_seq,"event_type":"edited","model_tier":model,"event_cost_usd":0.0,"event_latency_ms":0})
            ev_seq+=1; event_time+=timedelta(seconds=rng.randint(1,45)); final_event="accepted"
        else: final_event=outcome
        events.append({"event_id":f"EV{i:05d}_{ev_seq:02d}","request_id":request_id,"event_ts":event_time.isoformat(),
          "event_sequence":ev_seq,"event_type":final_event,"model_tier":model,"event_cost_usd":0.0,"event_latency_ms":0})
    req_df=pd.DataFrame(requests); event_df=pd.DataFrame(events)
    req_df.to_csv(out_dir/"ai_requests.csv",index=False); event_df.to_csv(out_dir/"interaction_events.csv",index=False)
    return req_df,event_df

if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--out",type=Path,default=ROOT/"data"); p.add_argument("--seed",type=int,default=SEED); p.add_argument("--requests",type=int,default=3000); a=p.parse_args()
    req,ev=generate(a.out,a.seed,a.requests); print({"requests":len(req),"events":len(ev)})
