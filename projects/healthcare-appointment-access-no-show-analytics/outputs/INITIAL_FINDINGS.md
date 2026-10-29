# Initial Findings — Appointment Access & No-show Analytics

**Generated:** 2026-10-29  
**Dataset:** Synthetic only; 7,200 appointment records, 2026-04-01 to 2026-09-27.

## KPI snapshot

- Scheduled appointment records: **7,200**
- Attended: **5,600**
- No-shows: **696**
- No-show rate among attended/no-show dispositions: **11.05%**
- Cancellation rate across all scheduled records: **7.90%**
- Average booking lead time: **11.00 days**
- Average wait among attended appointments: **25.26 minutes**
- Reminder coverage: **82.07%**

## Observed patterns in the generated scenario

- Highest clinic no-show rate: **Northside Medical Centre (12.62%)**.
- Highest specialty no-show rate: **Cardiology (12.42%)**.
- Reminder group rates: **No = 14.88%**, **Yes = 10.22%**. This is descriptive only: reminders are not randomly assigned in the generator, and the difference is not causal evidence.

## Stakeholder recommendations

1. Pilot confirmation and easy-reschedule workflows for clinics with above-network no-show rates.
2. Test shorter booking lead times or wait-list backfilling where the lead-time analysis suggests elevated risk.
3. Monitor wait times alongside attendance; a lower no-show rate does not automatically imply better access.
4. Before operational decisions, validate the same measures on real, governed appointment data and stratify by clinic, specialty, weekday, and booking lead time.

## Limitations

- All rows are generated with a fixed random seed; there is no real patient or provider information.
- Outcomes are simulated using explicit probability rules. Patterns are therefore partly built into the data and should not be generalized.
- No causal inference, patient-level prediction model, clinical conclusion, or financial savings estimate is provided.
- Appointment records are not linked into patient journeys; repeat-patient behavior cannot be assessed.
- No-show rate excludes Cancelled and Rescheduled records from its denominator; cancellation rate uses all scheduled records.
