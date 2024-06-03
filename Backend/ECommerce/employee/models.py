from django.contrib.auth.base_user import BaseUserManager
from django.db import models

from user.models import CustomUser


class UserManager(BaseUserManager):
    def create_user(self, username=None, password=None, **extra_fields):
        if username == '':
            raise ValueError('Укажите логин')
        user = self.model(username=username, **extra_fields)
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


class Employee(models.Model):
    POSITION_CHOICES = [
        ('админ', 'Админ'),
        ('продавец', 'Продавец'),
        ('бухгалтер', 'Бухгалтер'),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employee_profile')
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.jpg')
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, blank=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username