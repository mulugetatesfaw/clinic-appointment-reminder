
# admin.py
from django.contrib import admin
from .models import Appointment, Patient 
from doctor.models import Doctor, Availability

admin.site.site_header = "Clinic Admin Panel"
admin.site.site_title = "Clinic Admin"
admin.site.index_title = "Welcome to the Clinic Management System"


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    search_fields = ("name", "email")      


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "patient","created_at","date", "doctor", "reminder_sent")
    list_filter = ("date",)                 
    search_fields = ("patient__name", "patient__email")

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'specialty')


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'start_time', 'end_time')
    list_filter = ('doctor',)
