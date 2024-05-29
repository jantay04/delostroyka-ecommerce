from django.db import models


# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=50, verbose_name='ФИО')
    address = models.CharField(max_length=155, verbose_name='Адрес')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    email = models.EmailField(max_length=100, verbose_name='E-Mail')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')

    def __str__(self):
        return f'Name: {self.name}; ' \
               f'Address: {self.address}; ' \
               f'Phone: {self.phone}; ' \
               f'Email: {self.email}'