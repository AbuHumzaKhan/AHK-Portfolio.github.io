-- Each query should return zero rows or a zero-valued exception count.
SELECT appointment_id, COUNT(*) AS n FROM appointments GROUP BY appointment_id HAVING COUNT(*) > 1;
SELECT * FROM appointments WHERE lead_days < 0 OR date(appointment_date) < date(booking_date);
SELECT * FROM appointments WHERE status = 'Attended' AND wait_time_min IS NULL;
SELECT * FROM appointments WHERE status <> 'Attended' AND wait_time_min IS NOT NULL;
SELECT * FROM appointments WHERE reminder_sent NOT IN ('Yes','No');
SELECT * FROM appointments WHERE status NOT IN ('Attended','No-show','Cancelled','Rescheduled');
SELECT COUNT(*) AS missing_clinic_fk FROM appointments a LEFT JOIN clinics c USING (clinic_id) WHERE c.clinic_id IS NULL;
