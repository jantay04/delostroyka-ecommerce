from django.db import models

from apps.user.models import CustomUser


# Create your models here.
class Provider(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=155, verbose_name='Адрес')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')

    def __str__(self):
        return ''
