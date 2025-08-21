
import os
from django.utils import timezone
from django.core.mail import send_mail
from .models import Appointment
from core.gemini_client import generate_email_reminder

def send_appointment_reminders():
    now = timezone.now()
    reminder_time = now + timezone.timedelta(hours=3)

    upcoming_appointments = Appointment.objects.filter(
        date__range=(reminder_time, reminder_time + timezone.timedelta(hours=1))
    )

    for appt in upcoming_appointments:
        doctor_name = appt.doctor.name if appt.doctor else "Doctor (not assigned yet)"
        email_body = generate_email_reminder(
            patient_name=appt.patient.name,
            doctor_name=doctor_name,
            appointment_time=appt.date.strftime("%Y-%m-%d %H:%M")
        )
        send_mail(
            subject="Appointment Reminder",
            message=email_body,
            from_email=os.getenv("EMAIL_HOST_USER"),
            recipient_list=[appt.patient.email],
        )
        print(f"Sent reminder to {appt.patient.email} for appointment {appt.id} with {doctor_name}")

    print(send_appointment_reminders.__name__, "executed successfully")
