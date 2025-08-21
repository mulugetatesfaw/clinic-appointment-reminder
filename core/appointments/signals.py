from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Appointment
from doctor.models import Availability

@receiver(post_save, sender=Appointment)
def assign_doctor(sender, instance, created, **kwargs):
    if created and instance.doctor is None:
        # Find available doctors for this appointment date
        available = Availability.objects.filter(
            start_time__lte=instance.date,
            end_time__gte=instance.date
        ).order_by('start_time')

        if available.exists():
            instance.doctor = available.first().doctor
            instance.save()
            print(f"Assigned Doctor {instance.doctor.name} to appointment {instance.id}")
        else:
            print(f"No doctor available for appointment {instance.id}")
