"""Generate deterministic, entirely synthetic B2B SaaS operations data."""
from __future__ import annotations
import argparse, random
from datetime import date, timedelta
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
SEED=20261026

def generate(out_dir:Path=ROOT/"data",seed:int=SEED):
    rng=random.Random(seed); out_dir.mkdir(parents=True,exist_ok=True)
    segments=["SMB","Mid-Market","Enterprise"]; regions=["North","South","East","West"]; plans=["Starter","Growth","Scale"]
    accounts=[]
    for i in range(1,121):
        segment=rng.choices(segments,weights=[.48,.34,.18])[0]
        plan=rng.choices(plans,weights=[.45,.38,.17])[0]
        status=rng.choices(["active","trial","churned"],weights=[.77,.10,.13])[0]
        seats=rng.randint(3,35) if segment=="SMB" else (rng.randint(30,160) if segment=="Mid-Market" else rng.randint(150,600))
        rate={"Starter":900,"Growth":2400,"Scale":6800}[plan]
        mult={"SMB":1.0,"Mid-Market":2.4,"Enterprise":7.2}[segment]
        mcv=round(rate*mult*rng.uniform(.78,1.24),2)
        start=date(2024,1,1)+timedelta(days=rng.randint(0,950))
        accounts.append({"account_id":f"A{i:04d}","account_name":f"Synthetic Account {i:03d}","segment":segment,"region":rng.choice(regions),
          "plan_tier":plan,"account_status":status,"seats_purchased":seats,"start_date":start.isoformat(),
          "monthly_contract_value_inr":mcv,"account_manager":f"Manager-{rng.randint(1,8):02d}"})
    invoices=[]; inv_no=1
    for a in accounts:
        for month in range(4,10):
            inv_date=date(2026,month,1); status=rng.choices(["paid","open","void"],weights=[.80,.14,.06])[0]
            amount=round(a["monthly_contract_value_inr"]*rng.uniform(.96,1.04),2)
            invoices.append({"invoice_id":f"INV{inv_no:05d}","account_id":a["account_id"],"invoice_date":inv_date.isoformat(),
              "due_date":(inv_date+timedelta(days=14)).isoformat(),"invoice_status":status,"amount_inr":amount,
              "paid_amount_inr":amount if status=="paid" else 0.0})
            inv_no+=1
    usage=[]; d=date(2026,7,1)
    while d<=date(2026,9,30):
        for a in accounts:
            live=a["account_status"]!="churned"
            active=rng.randint(0,max(1,min(a["seats_purchased"],30))) if live and rng.random()<.72 else 0
            sessions=active*rng.randint(0,4)
            usage.append({"usage_date":d.isoformat(),"account_id":a["account_id"],"active_users":active,"sessions":sessions,"api_calls":sessions*rng.randint(1,18)})
        d+=timedelta(days=1)
    tickets=[]; categories=["Access","Billing","Integration","Performance","How-to"]
    for i in range(1,361):
        a=rng.choice(accounts); created=date(2026,7,1)+timedelta(days=rng.randint(0,91))
        priority=rng.choices(["low","medium","high"],weights=[.35,.46,.19])[0]
        status=rng.choices(["resolved","open","in_progress"],weights=[.74,.16,.10])[0]
        hours=round(rng.lognormvariate(2.1 if priority=="low" else (1.8 if priority=="medium" else 1.4),.55),2) if status=="resolved" else None
        resolved=(created+timedelta(days=max(0,int((hours or 0)//24)))).isoformat() if status=="resolved" else None
        tickets.append({"ticket_id":f"T{i:04d}","account_id":a["account_id"],"created_date":created.isoformat(),"resolved_date":resolved,
          "priority":priority,"status":status,"category":rng.choice(categories),"resolution_hours":hours})
    frames={"accounts":pd.DataFrame(accounts),"invoices":pd.DataFrame(invoices),"usage_daily":pd.DataFrame(usage),"support_tickets":pd.DataFrame(tickets)}
    for name,df in frames.items(): df.to_csv(out_dir/f"{name}.csv",index=False)
    return frames

if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--out",type=Path,default=ROOT/"data"); p.add_argument("--seed",type=int,default=SEED); a=p.parse_args()
    frames=generate(a.out,a.seed); print({k:len(v) for k,v in frames.items()})
