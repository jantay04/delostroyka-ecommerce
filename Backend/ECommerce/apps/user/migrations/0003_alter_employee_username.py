# Generated by Django 5.0 on 2024-05-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_managers_remove_client_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]