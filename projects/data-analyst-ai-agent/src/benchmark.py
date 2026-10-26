"""Run the known-answer benchmark in baseline and full-context modes."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import pandas as pd
from src.agent import execute_intent, format_answer, answer_question
ROOT = Path(__file__).resolve().parents[1]

def run_benchmark(db_path: Path = ROOT / "data" / "agent_demo.sqlite") -> tuple[pd.DataFrame, dict]:
    questions = json.loads((ROOT / "data" / "benchmark_questions.json").read_text(encoding="utf-8"))
    rows = []
    for item in questions:
        expected = format_answer(execute_intent(item["intent"], db_path))
        before = answer_question(item["question"], "baseline", db_path)["answer"]
        after = answer_question(item["question"], "full", db_path)["answer"]
        rows.append({"question_id": item["id"], "question": item["question"], "expected_intent": item["intent"],
                     "expected_answer": expected, "before_context_answer": before,
                     "before_correct": before == expected, "after_context_answer": after,
                     "after_correct": after == expected})
    df = pd.DataFrame(rows)
    summary = {
        "benchmark_questions": int(len(df)),
        "before_context_correct": int(df["before_correct"].sum()),
        "before_context_accuracy_pct": round(float(df["before_correct"].mean() * 100), 2),
        "after_context_correct": int(df["after_correct"].sum()),
        "after_context_accuracy_pct": round(float(df["after_correct"].mean() * 100), 2),
        "accuracy_lift_percentage_points": round(float((df["after_correct"].mean() - df["before_correct"].mean()) * 100), 2),
        "unanswered_before": int((df["before_context_answer"] == "UNANSWERED").sum()),
        "unanswered_after": int((df["after_context_answer"] == "UNANSWERED").sum()),
        "evaluation_note": "Deterministic intent-router/context ablation; not an LLM evaluation. Exact formatted answers are compared against known SQL-template outputs."
    }
    out = ROOT / "outputs"
    out.mkdir(exist_ok=True)
    df.to_csv(out / "benchmark_results.csv", index=False)
    (out / "benchmark_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return df, summary

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--db", type=Path, default=ROOT / "data" / "agent_demo.sqlite"); args = p.parse_args()
    _, summary = run_benchmark(args.db); print(json.dumps(summary, indent=2))
