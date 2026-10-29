PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS clinics;

CREATE TABLE clinics (
    clinic_id TEXT PRIMARY KEY,
    clinic_name TEXT NOT NULL UNIQUE
);

CREATE TABLE appointments (
    appointment_id TEXT PRIMARY KEY,
    appointment_date TEXT NOT NULL,
    booking_date TEXT NOT NULL,
    clinic_id TEXT NOT NULL REFERENCES clinics(clinic_id),
    clinic_name TEXT NOT NULL,
    specialty TEXT NOT NULL,
    appointment_type TEXT NOT NULL CHECK (appointment_type IN ('New','Follow-up')),
    lead_days INTEGER NOT NULL CHECK (lead_days >= 0),
    weekday TEXT NOT NULL,
    reminder_sent TEXT NOT NULL CHECK (reminder_sent IN ('Yes','No')),
    status TEXT NOT NULL CHECK (status IN ('Attended','No-show','Cancelled','Rescheduled')),
    scheduled_duration_min INTEGER NOT NULL CHECK (scheduled_duration_min > 0),
    wait_time_min REAL NULL CHECK (wait_time_min IS NULL OR wait_time_min >= 0),
    CHECK (date(appointment_date) >= date(booking_date)),
    CHECK ((status = 'Attended' AND wait_time_min IS NOT NULL) OR (status <> 'Attended' AND wait_time_min IS NULL))
);

CREATE INDEX idx_appointments_date ON appointments(appointment_date);
CREATE INDEX idx_appointments_clinic_status ON appointments(clinic_id, status);
CREATE INDEX idx_appointments_specialty ON appointments(specialty);
CREATE INDEX idx_appointments_reminder ON appointments(reminder_sent);
