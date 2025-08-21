from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer
from django.core.mail import send_mail

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer