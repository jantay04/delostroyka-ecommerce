from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if email == '':
            raise ValueError('Укажите почту')
        user = self.model(username=email, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


# Create your models here.
class CustomUser(AbstractUser):
    POSITION_CHOICES = [
        ('поставщик', 'Поставщик'),
        ('клиент', 'Клиент'),
        ('админ', 'Админ'),
        ('продавец', 'Продавец'),
        ('бухгалтер', 'Бухгалтер'),
    ]
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.jpg')
    full_name = models.CharField(max_length=30, blank=True, null=True)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, default=POSITION_CHOICES[0])
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    is_employee = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        if self.is_client:
            return f'Гость {self.pk}'
        elif self.is_employee:
            return f'Сотрудник {self.pk}'
        elif self.is_provider:
            return f'Поставщик {self.pk}'
        elif self.is_accountant:
            return f'Бухгалтер {self.pk}'
        elif self.is_admin:
            return f'Админ {self.pk}'
        elif self.is_seller:
            return f'Продавец {self.pk}'
        else:
            return f'User {self.pk}'


    def save(self, *args, **kwargs):
        if self.is_employee and self.is_client:
            raise ValueError("Пользователь не может быть и клиентом, и сотрудником одновременно.")

        super().save(*args, **kwargs)
