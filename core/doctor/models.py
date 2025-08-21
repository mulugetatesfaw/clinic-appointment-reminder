
# Create your models here.
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    specialty = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="availabilities")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.doctor.name}: {self.start_time} - {self.end_time}"

    def is_available(self, appointment_time):
        return self.start_time <= appointment_time <= self.end_time
