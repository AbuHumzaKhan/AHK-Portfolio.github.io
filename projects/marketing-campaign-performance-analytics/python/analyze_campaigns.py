#!/usr/bin/env python3
"""Recompute overall, campaign, and channel KPIs from the bundled synthetic CSVs."""
import csv, json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name):
    with (ROOT/'data'/name).open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f))
def agg(rows):
    s=lambda k:sum(float(r[k]) for r in rows)
    imp=int(s('impressions')); clicks=int(s('clicks')); spend=round(s('spend_usd'),2); conv=int(s('conversions')); rev=round(s('revenue_usd'),2); budget=round(s('daily_budget_usd'),2)
    return {'rows':len(rows),'impressions':imp,'clicks':clicks,'spend_usd':spend,'conversions':conv,'revenue_usd':rev,'budget_usd':budget,'ctr':clicks/imp if imp else 0,'cpc':spend/clicks if clicks else 0,'conversion_rate':conv/clicks if clicks else 0,'cpa':spend/conv if conv else 0,'roas':rev/spend if spend else 0,'budget_utilization':spend/budget if budget else 0}
def main():
    daily=load('campaign_daily_performance.csv'); campaigns=load('campaigns.csv')
    by_campaign={c['campaign_id']:agg([r for r in daily if r['campaign_id']==c['campaign_id']]) for c in campaigns}
    grouped=defaultdict(list)
    for r in daily: grouped[r['channel']].append(r)
    by_channel={k:agg(v) for k,v in sorted(grouped.items())}
    ranked=sorted(by_channel.items(),key=lambda x:x[1]['roas'],reverse=True)
    low=min([(c,by_campaign[c['campaign_id']]) for c in campaigns if by_campaign[c['campaign_id']]['conversions']>0],key=lambda x:x[1]['cpa'])
    high=max(campaigns,key=lambda c:by_campaign[c['campaign_id']]['spend_usd'])
    out={'scenario':{'seed':20261026,'start_date':min(r['date'] for r in daily),'end_date':max(r['date'] for r in daily),'daily_rows':len(daily),'campaigns':len(campaigns),'channels':len(by_channel),'synthetic':True},'overall':agg(daily),'top_channel_by_roas':{'channel':ranked[0][0],'roas':round(ranked[0][1]['roas'],3),'spend_usd':ranked[0][1]['spend_usd'],'revenue_usd':ranked[0][1]['revenue_usd']},'lowest_cpa_campaign':{'campaign':low[0]['campaign_name'],'channel':low[0]['channel'],'cpa_usd':round(low[1]['cpa'],2),'conversions':low[1]['conversions']},'highest_spend_campaign':{'campaign':high['campaign_name'],'spend_usd':by_campaign[high['campaign_id']]['spend_usd']},'campaigns':[{'campaign_id':c['campaign_id'],'campaign_name':c['campaign_name'],'channel':c['channel'],**{k:round(v,4) if isinstance(v,float) else v for k,v in by_campaign[c['campaign_id']].items()}} for c in campaigns],'channels':[{'channel':ch,**{k:round(v,4) if isinstance(v,float) else v for k,v in by_channel[ch].items()}} for ch in by_channel]}
    (ROOT/'outputs').mkdir(exist_ok=True)
    (ROOT/'outputs'/'metrics_summary.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('Metrics recomputed; campaign-day rows:',len(daily),'portfolio ROAS:',round(out['overall']['roas'],2))
if __name__=='__main__': main()