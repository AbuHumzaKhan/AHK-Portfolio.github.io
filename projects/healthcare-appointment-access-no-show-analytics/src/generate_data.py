"""Generate a reproducible, fully synthetic outpatient appointment dataset.
No real patient data is used. Run from the project root: python src/generate_data.py
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261029
START_DATE = "2026-04-01"
END_DATE = "2026-09-27"
APPOINTMENTS_PER_DAY = 40

CLINICS = [
    ("CL-01", "Central Family Clinic", 0.020, 1.5),
    ("CL-02", "Northside Medical Centre", 0.012, 4.0),
    ("CL-03", "Riverside Outpatient", -0.010, -1.0),
    ("CL-04", "Eastgate Clinic", 0.006, 2.0),
    ("CL-05", "West End Health Hub", -0.004, 0.5),
    ("CL-06", "Lakeside Specialty Centre", 0.014, 3.0),
]
SPECIALTIES = ["General Practice", "Cardiology", "Dermatology", "Orthopedics", "Pediatrics", "ENT", "Ophthalmology", "Physiotherapy"]
SPECIALTY_EFFECT = {"General Practice": 0.000, "Cardiology": 0.012, "Dermatology": -0.008, "Orthopedics": 0.010, "Pediatrics": -0.004, "ENT": 0.003, "Ophthalmology": 0.005, "Physiotherapy": 0.008}


def generate() -> pd.DataFrame:
    rng = np.random.default_rng(SEED)
    dates = pd.date_range(START_DATE, END_DATE, freq="D")
    n = len(dates) * APPOINTMENTS_PER_DAY
    appointment_dates = np.repeat(dates.to_numpy(), APPOINTMENTS_PER_DAY)
    clinic_idx = rng.choice(len(CLINICS), n, p=[0.20, 0.18, 0.16, 0.16, 0.15, 0.15])
    specialty = rng.choice(SPECIALTIES, n, p=[0.26, 0.12, 0.11, 0.13, 0.12, 0.09, 0.08, 0.09])
    appointment_type = rng.choice(["New", "Follow-up"], n, p=[0.38, 0.62])
    lead_days = np.clip(rng.gamma(shape=2.0, scale=5.5, size=n).round().astype(int), 0, 60)
    booking_dates = pd.to_datetime(appointment_dates) - pd.to_timedelta(lead_days, unit="D")
    weekdays = pd.to_datetime(appointment_dates).day_name()
    reminder_probability = np.where(lead_days >= 2, 0.84, 0.32)
    reminder_sent = rng.random(n) < reminder_probability
    clinic_effect = np.array([CLINICS[i][2] for i in clinic_idx])
    clinic_wait_effect = np.array([CLINICS[i][3] for i in clinic_idx])
    weekend_effect = np.isin(weekdays, ["Saturday", "Sunday"]) * 0.006
    monday_effect = (weekdays == "Monday") * 0.018
    followup_effect = (appointment_type == "Follow-up") * -0.014
    lead_effect = np.minimum(lead_days, 30) * 0.0017
    reminder_effect = reminder_sent * -0.043
    spec_effect = np.array([SPECIALTY_EFFECT[s] for s in specialty])
    no_show_prob = np.clip(0.105 + clinic_effect + weekend_effect + monday_effect + followup_effect + lead_effect + reminder_effect + spec_effect, 0.025, 0.32)
    cancellation_prob = np.clip(0.064 + np.minimum(lead_days, 30) * 0.0009 + (appointment_type == "New") * 0.012, 0.04, 0.13)
    reschedule_prob = np.full(n, 0.045)
    p_attend = 1 - no_show_prob - cancellation_prob - reschedule_prob
    probabilities = np.column_stack([p_attend, no_show_prob, cancellation_prob, reschedule_prob])
    statuses = np.array(["Attended", "No-show", "Cancelled", "Rescheduled"])
    status = np.array([rng.choice(statuses, p=p / p.sum()) for p in probabilities])
    duration = rng.choice([15, 20, 30, 45, 60], n, p=[0.08, 0.08, 0.47, 0.22, 0.15])
    wait = np.maximum(0, rng.normal(23 + clinic_wait_effect + np.array([SPECIALTY_EFFECT[s] * 100 for s in specialty]), 9, n)).round(0)
    wait_time = np.where(status == "Attended", wait, np.nan)
    clinic_ids = [CLINICS[i][0] for i in clinic_idx]
    clinic_names = [CLINICS[i][1] for i in clinic_idx]
    return pd.DataFrame({
        "appointment_id": [f"APT-{i:06d}" for i in range(1, n + 1)],
        "appointment_date": pd.to_datetime(appointment_dates).strftime("%Y-%m-%d"),
        "booking_date": pd.to_datetime(booking_dates).strftime("%Y-%m-%d"),
        "clinic_id": clinic_ids,
        "clinic_name": clinic_names,
        "specialty": specialty,
        "appointment_type": appointment_type,
        "lead_days": lead_days,
        "weekday": weekdays,
        "reminder_sent": np.where(reminder_sent, "Yes", "No"),
        "status": status,
        "scheduled_duration_min": duration,
        "wait_time_min": wait_time,
    })


def main() -> None:
    (ROOT / "data").mkdir(exist_ok=True)
    df = generate()
    df.to_csv(ROOT / "data" / "appointments_synthetic.csv", index=False)
    print(f"Generated {len(df):,} synthetic appointments: {df.appointment_date.min()} to {df.appointment_date.max()}")

if __name__ == "__main__":
    main()
