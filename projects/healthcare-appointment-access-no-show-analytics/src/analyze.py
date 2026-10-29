"""Analysis pipeline for the synthetic appointment operations project."""
from __future__ import annotations
import json
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "appointments_synthetic.csv"
OUT = ROOT / "outputs"
REPORTS = ROOT / "reports"


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA, parse_dates=["appointment_date", "booking_date"])
    df["is_disposition_denominator"] = df["status"].isin(["Attended", "No-show"])
    df["is_no_show"] = df["status"].eq("No-show")
    df["week_start"] = df["appointment_date"].dt.to_period("W-SUN").apply(lambda p: p.start_time).dt.strftime("%Y-%m-%d")
    bins = [-1, 1, 7, 14, 30, 60]
    labels = ["0-1 days", "2-7 days", "8-14 days", "15-30 days", "31-60 days"]
    df["lead_time_band"] = pd.cut(df["lead_days"], bins=bins, labels=labels)
    return df


def summary(df: pd.DataFrame) -> dict:
    eligible = df[df.is_disposition_denominator]
    total = len(df)
    attended = int(df.status.eq("Attended").sum())
    no_show = int(df.status.eq("No-show").sum())
    cancelled = int(df.status.eq("Cancelled").sum())
    rescheduled = int(df.status.eq("Rescheduled").sum())
    return {
        "dataset": {"rows": total, "start_date": df.appointment_date.min().strftime("%Y-%m-%d"), "end_date": df.appointment_date.max().strftime("%Y-%m-%d"), "clinics": int(df.clinic_id.nunique()), "specialties": int(df.specialty.nunique())},
        "kpis": {
            "scheduled_appointments": total, "attended": attended, "no_shows": no_show,
            "cancelled": cancelled, "rescheduled": rescheduled,
            "no_show_rate_pct": round(no_show / max(len(eligible), 1) * 100, 2),
            "attendance_rate_pct": round(attended / max(len(eligible), 1) * 100, 2),
            "cancellation_rate_pct": round(cancelled / max(total, 1) * 100, 2),
            "reschedule_rate_pct": round(rescheduled / max(total, 1) * 100, 2),
            "avg_lead_days": round(float(df.lead_days.mean()), 2),
            "avg_wait_min_attended": round(float(df.loc[df.status.eq("Attended"), "wait_time_min"].mean()), 2),
            "reminder_coverage_pct": round(df.reminder_sent.eq("Yes").mean() * 100, 2),
        },
        "definitions": {
            "no_show_rate": "No-show / (Attended + No-show). Cancelled and Rescheduled are excluded from this denominator.",
            "attendance_rate": "Attended / (Attended + No-show). Cancelled and Rescheduled are excluded.",
            "cancellation_rate": "Cancelled / all scheduled appointment records.",
            "reminder_comparison": "Descriptive association only; reminder delivery is not randomized and must not be interpreted as causal impact."
        }
    }


def group_metrics(df: pd.DataFrame, col: str) -> pd.DataFrame:
    g = df.groupby(col, observed=True).agg(
        appointments=("appointment_id", "size"),
        attended=("status", lambda x: int((x == "Attended").sum())),
        no_shows=("status", lambda x: int((x == "No-show").sum())),
        cancelled=("status", lambda x: int((x == "Cancelled").sum())),
        rescheduled=("status", lambda x: int((x == "Rescheduled").sum())),
        avg_lead_days=("lead_days", "mean"),
        avg_wait_min=("wait_time_min", "mean"),
    ).reset_index()
    g["eligible"] = g["attended"] + g["no_shows"]
    g["no_show_rate_pct"] = (g["no_shows"] / g["eligible"].replace(0, pd.NA) * 100).fillna(0).round(2)
    g["attendance_rate_pct"] = (g["attended"] / g["eligible"].replace(0, pd.NA) * 100).fillna(0).round(2)
    g["avg_lead_days"] = g["avg_lead_days"].round(2)
    g["avg_wait_min"] = g["avg_wait_min"].round(2)
    return g.drop(columns=["eligible"])


def main() -> None:
    OUT.mkdir(exist_ok=True); REPORTS.mkdir(exist_ok=True)
    df = load_data()
    metrics = summary(df)
    (OUT / "metrics_summary.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    for col, filename in [("clinic_name", "clinic_summary.csv"), ("specialty", "specialty_summary.csv"), ("weekday", "weekday_summary.csv"), ("lead_time_band", "lead_time_summary.csv"), ("reminder_sent", "reminder_summary.csv"), ("week_start", "weekly_summary.csv")]:
        group_metrics(df, col).to_csv(OUT / filename, index=False)
    records = df.groupby(["clinic_name", "specialty", "status"], observed=True).agg(
        count=("appointment_id", "size"), wait_sum=("wait_time_min", lambda s: float(s.fillna(0).sum())),
        wait_n=("wait_time_min", "count"), lead_sum=("lead_days", "sum")
    ).reset_index()
    compact = [{"c": r.clinic_name, "s": r.specialty, "t": r.status, "n": int(r.count), "ws": float(r.wait_sum), "wn": int(r.wait_n), "ls": int(r.lead_sum)} for r in records.itertuples(index=False)]
    dashboard_data = {
        "segments": compact,
        "weekday": pd.read_csv(OUT / "weekday_summary.csv").rename(columns={"weekday": "name"}).to_dict(orient="records"),
        "lead": pd.read_csv(OUT / "lead_time_summary.csv").rename(columns={"lead_time_band": "name"}).to_dict(orient="records"),
        "reminder": pd.read_csv(OUT / "reminder_summary.csv").rename(columns={"reminder_sent": "name"}).to_dict(orient="records"),
        "clinics": pd.read_csv(OUT / "clinic_summary.csv").rename(columns={"clinic_name": "name"}).to_dict(orient="records"),
        "specialties": pd.read_csv(OUT / "specialty_summary.csv").rename(columns={"specialty": "name"}).to_dict(orient="records"),
    }
    (OUT / "dashboard_aggregates.json").write_text(json.dumps(dashboard_data, separators=(",", ":")), encoding="utf-8")
    clinic = pd.read_csv(OUT / "clinic_summary.csv").sort_values("no_show_rate_pct", ascending=False)
    plt.figure(figsize=(9, 4.8))
    plt.bar(clinic["clinic_name"], clinic["no_show_rate_pct"])
    plt.title("No-show rate by clinic (eligible dispositions only)"); plt.ylabel("No-show rate (%)"); plt.xticks(rotation=25, ha="right"); plt.tight_layout()
    plt.savefig(REPORTS / "no_show_by_clinic.png", dpi=150); plt.close()
    lead = pd.read_csv(OUT / "lead_time_summary.csv")
    plt.figure(figsize=(8, 4.5))
    plt.bar(lead["lead_time_band"].astype(str), lead["no_show_rate_pct"])
    plt.title("No-show rate by booking lead time"); plt.ylabel("No-show rate (%)"); plt.xticks(rotation=20, ha="right"); plt.tight_layout()
    plt.savefig(REPORTS / "no_show_by_lead_time.png", dpi=150); plt.close()
    specialty = pd.read_csv(OUT / "specialty_summary.csv").sort_values("no_show_rate_pct", ascending=False).iloc[0]
    reminder = pd.read_csv(OUT / "reminder_summary.csv").set_index("reminder_sent")
    reminder_rates = {str(k): float(v) for k, v in reminder["no_show_rate_pct"].to_dict().items()}
    findings = f"""# Initial Findings — Appointment Access & No-show Analytics

**Generated:** 2026-10-29  
**Dataset:** Synthetic only; {metrics['dataset']['rows']:,} appointment records, {metrics['dataset']['start_date']} to {metrics['dataset']['end_date']}.

## KPI snapshot

- Scheduled appointment records: **{metrics['kpis']['scheduled_appointments']:,}**
- Attended: **{metrics['kpis']['attended']:,}**
- No-shows: **{metrics['kpis']['no_shows']:,}**
- No-show rate among attended/no-show dispositions: **{metrics['kpis']['no_show_rate_pct']:.2f}%**
- Cancellation rate across all scheduled records: **{metrics['kpis']['cancellation_rate_pct']:.2f}%**
- Average booking lead time: **{metrics['kpis']['avg_lead_days']:.2f} days**
- Average wait among attended appointments: **{metrics['kpis']['avg_wait_min_attended']:.2f} minutes**
- Reminder coverage: **{metrics['kpis']['reminder_coverage_pct']:.2f}%**

## Observed patterns in the generated scenario

- Highest clinic no-show rate: **{clinic.iloc[0]['clinic_name']} ({clinic.iloc[0]['no_show_rate_pct']:.2f}%)**.
- Highest specialty no-show rate: **{specialty['specialty']} ({specialty['no_show_rate_pct']:.2f}%)**.
- Reminder group rates: **No = {reminder_rates.get('No', 0):.2f}%**, **Yes = {reminder_rates.get('Yes', 0):.2f}%**. This is descriptive only and not causal evidence.

## Stakeholder recommendations

1. Pilot confirmation and easy-reschedule workflows for clinics with above-network no-show rates.
2. Test shorter booking lead times or wait-list backfilling where the lead-time analysis suggests elevated risk.
3. Monitor wait times alongside attendance; a lower no-show rate does not automatically imply better access.
4. Validate these measures on real, governed operational data before changing policy.

## Limitations

- All rows are synthetic; no real patient or provider information is included.
- Outcomes follow explicit probability rules, so some segment patterns are built into the data.
- No causal inference, patient-level prediction, clinical conclusion, or savings estimate is provided.
- Appointment records are not linked into patient journeys; repeat-patient behavior cannot be assessed.
- No-show rate excludes Cancelled and Rescheduled records from its denominator.
"""
    (OUT / "INITIAL_FINDINGS.md").write_text(findings, encoding="utf-8")
    print(json.dumps(metrics["kpis"], indent=2))

if __name__ == "__main__":
    main()
