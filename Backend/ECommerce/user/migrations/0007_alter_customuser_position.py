# Generated by Django 5.0.6 on 2024-06-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_customuser_full_name_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='position',
            field=models.CharField(choices=[('клиент', 'Клиент'), ('админ', 'Админ'), ('продавец', 'Продавец'), ('бухгалтер', 'Бухгалтер')], default=('клиент', 'Клиент'), max_length=50),
        ),
    ]
