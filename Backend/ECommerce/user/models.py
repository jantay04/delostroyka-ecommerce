from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return f'User ID{self.pk}'

    def save(self, *args, **kwargs):
        if self.is_employee and self.is_client:
            raise ValueError("Пользователь не может быть и клиентом, и сотрудником одновременно.")

        super().save(*args, **kwargs)


