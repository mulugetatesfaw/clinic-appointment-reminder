from django.db import models
from patients.models import Patient
from doctor.models import Doctor ,Availability
from django.utils import timezone
from datetime import timedelta

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name="appointments")
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    reminder_sent = models.BooleanField(default=False)  # to track if email reminder was sent

    def __str__(self):
        doctor_name = self.doctor.name if self.doctor else "Unassigned"
        return f"Appointment for {self.patient.name} with {doctor_name} on {self.date}"

    def is_within_24_hours(self):
        return timezone.now() >= self.date - timedelta(hours=24)
