from django.core.validators import RegexValidator
from django.db import models

from user.models import CustomUser


# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='client_profile')
    full_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'Client ID: {self.pk}; email: {self.email}'
