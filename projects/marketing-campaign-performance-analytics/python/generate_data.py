#!/usr/bin/env python3
"""Generate deterministic synthetic campaign CSVs, SQL seed data, and SQLite database."""
import csv, math, random, sqlite3
from datetime import date, timedelta
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SEED=20261026
CAMPAIGNS=[
 dict(campaign_id='C001',campaign_name='Brand Search',channel='Paid Search',objective='Purchase',audience_segment='High Intent',daily_budget_usd=800.0,base_impressions=8200,ctr=.072,cpc=1.18,cvr=.092,aov=92.0),
 dict(campaign_id='C002',campaign_name='Generic Search',channel='Paid Search',objective='Purchase',audience_segment='High Intent',daily_budget_usd=1200.0,base_impressions=14500,ctr=.043,cpc=1.72,cvr=.058,aov=84.0),
 dict(campaign_id='C003',campaign_name='Social Prospecting',channel='Paid Social',objective='Purchase',audience_segment='New Audiences',daily_budget_usd=500.0,base_impressions=27000,ctr=.016,cpc=.78,cvr=.026,aov=76.0),
 dict(campaign_id='C004',campaign_name='Social Retargeting',channel='Paid Social',objective='Purchase',audience_segment='Returning Visitors',daily_budget_usd=300.0,base_impressions=11500,ctr=.031,cpc=.64,cvr=.071,aov=88.0),
 dict(campaign_id='C005',campaign_name='Display Retargeting',channel='Display',objective='Purchase',audience_segment='Returning Visitors',daily_budget_usd=180.0,base_impressions=34000,ctr=.0075,cpc=.42,cvr=.035,aov=81.0),
 dict(campaign_id='C006',campaign_name='Lifecycle Email',channel='Email',objective='Purchase',audience_segment='Existing Customers',daily_budget_usd=180.0,base_impressions=18500,ctr=.055,cpc=.14,cvr=.035,aov=69.0),
 dict(campaign_id='C007',campaign_name='Affiliate Partners',channel='Affiliate',objective='Purchase',audience_segment='Partner Referred',daily_budget_usd=220.0,base_impressions=7800,ctr=.039,cpc=.52,cvr=.064,aov=95.0),
 dict(campaign_id='C008',campaign_name='Video Awareness',channel='Online Video',objective='Consideration',audience_segment='New Audiences',daily_budget_usd=180.0,base_impressions=42000,ctr=.0055,cpc=.53,cvr=.012,aov=70.0)]
FIELDS=['date','campaign_id','campaign_name','channel','objective','audience_segment','impressions','clicks','spend_usd','conversions','revenue_usd','daily_budget_usd']
def main():
    (ROOT/'data').mkdir(exist_ok=True); (ROOT/'sql').mkdir(exist_ok=True)
    rng=random.Random(SEED); rows=[]
    for i in range(84):
        d=date(2026,7,6)+timedelta(days=i); dow=d.weekday(); trend=.94+.0018*i
        for c in CAMPAIGNS:
            weekend=(.84 if c['channel']=='Paid Search' else 1.12) if dow>=5 else 1.0
            if c['channel']=='Email' and dow in (1,2,3): weekend*=1.14
            lift=1.12 if date(2026,8,15)<=d<=date(2026,8,20) else 1.0
            imp=max(100,int(rng.gauss(c['base_impressions']*trend*weekend*lift,c['base_impressions']*.085)))
            ctr=max(.001,rng.gauss(c['ctr']*(1.04 if dow in (1,2) else 1),c['ctr']*.075))
            clicks=min(imp,max(0,int(round(rng.gauss(imp*ctr,math.sqrt(max(1,imp*ctr*(1-ctr))))))))
            cpc=max(.02,rng.gauss(c['cpc'],c['cpc']*.09))
            spend=round(max(.01,clicks*cpc+rng.uniform(0,c['daily_budget_usd']*.035)),2)
            cvr=max(.001,rng.gauss(c['cvr']*(1.05 if dow in (1,2,3) else 1),c['cvr']*.10))
            conv=max(0,int(round(rng.gauss(clicks*cvr,math.sqrt(max(1,clicks*cvr*(1-cvr)))))))
            aov=max(15,rng.gauss(c['aov'],c['aov']*.08))
            revenue=round(max(0,conv*aov*rng.uniform(.96,1.04)),2)
            rows.append(dict(date=d.isoformat(),campaign_id=c['campaign_id'],campaign_name=c['campaign_name'],channel=c['channel'],objective=c['objective'],audience_segment=c['audience_segment'],impressions=imp,clicks=clicks,spend_usd=spend,conversions=conv,revenue_usd=revenue,daily_budget_usd=c['daily_budget_usd']))
    with (ROOT/'data'/'campaigns.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=['campaign_id','campaign_name','channel','objective','audience_segment','daily_budget_usd']); w.writeheader(); w.writerows([{k:c[k] for k in w.fieldnames} for c in CAMPAIGNS])
    with (ROOT/'data'/'campaign_daily_performance.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows(rows)
    def q(v): return "'" + str(v).replace("'","''") + "'" if isinstance(v,str) else str(v)
    lines=['-- Synthetic seed data; run after sql/schema.sql.']
    lines.append('INSERT INTO campaigns (campaign_id,campaign_name,channel,objective,audience_segment,daily_budget_usd) VALUES\n'+',\n'.join('('+','.join(q(c[k]) for k in ['campaign_id','campaign_name','channel','objective','audience_segment','daily_budget_usd'])+')' for c in CAMPAIGNS)+';')
    lines.append('INSERT INTO campaign_daily_performance (date,campaign_id,impressions,clicks,spend_usd,conversions,revenue_usd) VALUES\n'+',\n'.join('('+','.join(q(r[k]) for k in ['date','campaign_id','impressions','clicks','spend_usd','conversions','revenue_usd'])+')' for r in rows)+';')
    (ROOT/'sql'/'seed_data.sql').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    db=ROOT/'data'/'marketing_campaigns.sqlite'
    if db.exists(): db.unlink()
    con=sqlite3.connect(db)
    try:
        con.executescript((ROOT/'sql'/'schema.sql').read_text(encoding='utf-8'))
        con.executescript((ROOT/'sql'/'seed_data.sql').read_text(encoding='utf-8')); con.commit()
    finally: con.close()
    print('Generated 672 campaign-day rows for 8 campaigns with seed 20261026.')
if __name__=='__main__': main()