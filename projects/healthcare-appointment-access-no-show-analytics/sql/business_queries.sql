-- 1) Executive KPI snapshot. No-show denominator excludes cancellations/reschedules.
SELECT COUNT(*) AS scheduled_appointment_records,
       SUM(CASE WHEN status = 'Attended' THEN 1 ELSE 0 END) AS attended,
       SUM(CASE WHEN status = 'No-show' THEN 1 ELSE 0 END) AS no_shows,
       ROUND(100.0 * SUM(CASE WHEN status = 'No-show' THEN 1 ELSE 0 END) /
         NULLIF(SUM(CASE WHEN status IN ('Attended','No-show') THEN 1 ELSE 0 END), 0), 2) AS no_show_rate_pct,
       ROUND(100.0 * SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) / COUNT(*), 2) AS cancellation_rate_pct,
       ROUND(AVG(lead_days), 2) AS avg_lead_days,
       ROUND(AVG(CASE WHEN status = 'Attended' THEN wait_time_min END), 2) AS avg_wait_min_attended
FROM appointments;

-- 2) Clinic performance.
SELECT clinic_name, COUNT(*) AS appointments,
       SUM(status = 'Attended') AS attended,
       SUM(status = 'No-show') AS no_shows,
       ROUND(100.0 * SUM(status = 'No-show') / NULLIF(SUM(status IN ('Attended','No-show')),0), 2) AS no_show_rate_pct,
       ROUND(AVG(CASE WHEN status = 'Attended' THEN wait_time_min END), 2) AS avg_wait_min
FROM appointments GROUP BY clinic_name ORDER BY no_show_rate_pct DESC;

-- 3) No-show rates by specialty.
SELECT specialty, COUNT(*) AS appointments, SUM(status = 'No-show') AS no_shows,
       ROUND(100.0 * SUM(status = 'No-show') / NULLIF(SUM(status IN ('Attended','No-show')),0), 2) AS no_show_rate_pct
FROM appointments GROUP BY specialty ORDER BY no_show_rate_pct DESC;

-- 4) Lead-time bands.
SELECT CASE WHEN lead_days <= 1 THEN '0-1 days'
            WHEN lead_days <= 7 THEN '2-7 days'
            WHEN lead_days <= 14 THEN '8-14 days'
            WHEN lead_days <= 30 THEN '15-30 days'
            ELSE '31-60 days' END AS lead_time_band,
       COUNT(*) AS appointments, SUM(status = 'No-show') AS no_shows,
       ROUND(100.0 * SUM(status = 'No-show') / NULLIF(SUM(status IN ('Attended','No-show')),0), 2) AS no_show_rate_pct
FROM appointments GROUP BY lead_time_band ORDER BY MIN(lead_days);

-- 5) Reminder group comparison. Descriptive, not causal.
SELECT reminder_sent, COUNT(*) AS appointments, SUM(status = 'No-show') AS no_shows,
       ROUND(100.0 * SUM(status = 'No-show') / NULLIF(SUM(status IN ('Attended','No-show')),0), 2) AS no_show_rate_pct
FROM appointments GROUP BY reminder_sent;

-- 6) Weekly operational trend.
SELECT date(appointment_date, '-' || ((CAST(strftime('%w', appointment_date) AS INTEGER) + 6) % 7) || ' days') AS week_start,
       COUNT(*) AS appointments, SUM(status = 'No-show') AS no_shows,
       ROUND(100.0 * SUM(status = 'No-show') / NULLIF(SUM(status IN ('Attended','No-show')),0), 2) AS no_show_rate_pct
FROM appointments GROUP BY week_start ORDER BY week_start;

-- 7) Clinic-specialty combinations with at least 50 eligible outcomes.
SELECT clinic_name, specialty, COUNT(*) AS appointments, SUM(status = 'No-show') AS no_shows,
       ROUND(100.0 * SUM(status = 'No-show') / NULLIF(SUM(status IN ('Attended','No-show')),0), 2) AS no_show_rate_pct
FROM appointments GROUP BY clinic_name, specialty
HAVING SUM(status IN ('Attended','No-show')) >= 50
ORDER BY no_show_rate_pct DESC, appointments DESC;
