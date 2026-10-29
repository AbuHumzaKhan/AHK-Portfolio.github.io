# Data Dictionary

All records are synthetic and generated locally with a fixed seed (`20261029`). No real patient, clinician, or facility data is used.

| Column | Type | Definition | Quality rule |
|---|---|---|---|
| `appointment_id` | Text | Unique synthetic appointment-record identifier | Unique and non-null |
| `appointment_date` | Date | Scheduled date | Between 2026-04-01 and 2026-09-27 |
| `booking_date` | Date | Date the appointment was booked | On or before appointment date |
| `clinic_id` | Text | Synthetic clinic key | Must match `clinics` dimension |
| `clinic_name` | Text | Synthetic clinic label | Six generated clinics |
| `specialty` | Category | Appointment specialty | One of eight generated categories |
| `appointment_type` | Category | New or Follow-up appointment | Controlled category |
| `lead_days` | Integer | Days between booking and appointment date | Non-negative |
| `weekday` | Category | Day of week of scheduled appointment | Derived from appointment date |
| `reminder_sent` | Category | Whether the synthetic scenario marks a reminder as sent | `Yes` or `No`; not proof of delivery |
| `status` | Category | Attended, No-show, Cancelled, or Rescheduled | Controlled category |
| `scheduled_duration_min` | Integer | Planned slot length in minutes | Positive integer |
| `wait_time_min` | Number / null | Wait time for attended appointments | Present only when status is Attended |

## Metric definitions

- **No-show rate:** `No-show / (Attended + No-show)`. Cancelled and Rescheduled records are excluded from the denominator.
- **Attendance rate:** `Attended / (Attended + No-show)`.
- **Cancellation rate:** `Cancelled / all scheduled appointment records`.
- **Reminder coverage:** Records marked `Yes` divided by all scheduled records.
- **Average wait time:** Mean wait time for attended appointments only.

The synthetic appointment record is not a patient-level entity and does not support longitudinal patient analysis.
