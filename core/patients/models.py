from django.db import models
class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.name
