"""Minimal local FastAPI interface for the context-aware agent."""
from html import escape
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from src.agent import answer_question
app=FastAPI(title="Context-Aware Data Analyst Agent",version="1.0.0")
PAGE="""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>Context-Aware Data Analyst Agent</title><style>body{font-family:Segoe UI,Arial;background:#0b1020;color:#eaf0ff;padding:28px;max-width:900px;margin:auto}section{background:#121b31;border:1px solid #293959;border-radius:16px;padding:22px;margin:18px 0}p{color:#a8b7d7;line-height:1.6}input,select,button{font:inherit;padding:12px;border-radius:9px;border:1px solid #39506f;background:#0b1224;color:#fff}input{width:55%}button{background:#5b8cff;cursor:pointer}.answer{padding:14px;background:#091426;border-left:4px solid #46d7ad}</style></head><body><small>PROJECT 04 · SYNTHETIC DATA · NO PAID API</small><h1>Context-Aware Data Analyst Agent</h1><p>Ask a supported question about the fictional SaaS dataset. The prototype selects an allow-listed SQL template; it does not call an external model.</p><section><form action='/ask' method='post'><input name='question' value='{{question}}' placeholder='What is MRR?' required><select name='mode'><option value='full' {{full}}>Full context</option><option value='baseline' {{baseline}}>Baseline</option></select><button>Analyze</button></form><p class='answer'>{{answer}}</p><p>As-of date: 2026-10-01. Benchmark is a deterministic context ablation, not a general LLM benchmark.</p></section></body></html>"""
@app.get("/health")
def health():
    return {"status":"ok","data":"synthetic","llm":False}
@app.get("/",response_class=HTMLResponse)
def home():
    return HTMLResponse(PAGE.replace("{{question}}","").replace("{{answer}}","Try “What is MRR?”").replace("{{full}}","selected").replace("{{baseline}}",""))
@app.post("/ask",response_class=HTMLResponse)
def ask(question:str=Form(...),mode:str=Form("full")):
    result=answer_question(question,mode=mode)
    answer=f"Intent: {escape(str(result['intent'] or 'not recognized'))}<br>Answer: {escape(str(result['answer']))}"
    return HTMLResponse(PAGE.replace("{{question}}",escape(question,quote=True)).replace("{{answer}}",answer).replace("{{full}}","selected" if mode=="full" else "").replace("{{baseline}}","selected" if mode=="baseline" else ""))
