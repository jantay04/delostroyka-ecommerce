# Generated by Django 5.0.6 on 2024-05-27 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='media/avatars/default_avatar.jpg', upload_to='avatars/'),
        ),
    ]
