from django.db import models


# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=155)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Name: {self.name}; ' \
               f'Address: {self.address}; ' \
               f'Phone: {self.phone}; ' \
               f'Email: {self.email}'