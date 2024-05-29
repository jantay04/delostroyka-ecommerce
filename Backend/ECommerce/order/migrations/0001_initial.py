# Generated by Django 5.0.6 on 2024-05-29 10:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_alter_category_created_at_alter_category_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_address_line_1', models.CharField(default='Адрес не указан', max_length=255, verbose_name='Адрес')),
                ('shipping_address_line_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес (дополнительный)')),
                ('shipping_city', models.CharField(default='Город не указан', max_length=100, verbose_name='Город')),
                ('shipping_postal_code', models.CharField(default='Почтовый код не указан', max_length=35, verbose_name='Почтовый код')),
                ('shipping_country', models.CharField(default='Страна не указана', max_length=100, verbose_name='Страна')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Кол-во')),
                ('status', models.CharField(choices=[('Ожидание оплаты', 'Ожидание оплаты'), ('В процессе..', 'В процессе..'), ('Удержание', 'Удержание'), ('Завершено', 'Завершено'), ('Отменено', 'Отменено'), ('Возврат', 'Возврат'), ('Провален', 'Провален'), ('Заметки', 'Заметки')], default='Заметки', verbose_name='Статус заказа')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Кол-во')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Товар')),
            ],
        ),
    ]
