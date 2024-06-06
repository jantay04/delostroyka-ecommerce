from django.db import models


from apps.product.models import Product
from apps.user.models import CustomUser


# Create your models here.
class Order(models.Model):
    PENDING_PAYMENT = 'Ожидание оплаты'
    PROCESSING = 'В процессе..'
    ON_HOLD = 'Удержание'
    COMPLETED = 'Завершено'
    CANCELLED = 'Отменено'
    REFUNDED = 'Возврат'
    FAILED = 'Провален'
    DRAFT = 'Заметки'

    ORDER_STATUS_CHOICES = [
        (PENDING_PAYMENT, 'Ожидание оплаты'),
        (PROCESSING, 'В процессе..'),
        (ON_HOLD, 'Удержание'),
        (COMPLETED, 'Завершено'),
        (CANCELLED, 'Отменено'),
        (REFUNDED, 'Возврат'),
        (FAILED, 'Провален'),
        (DRAFT, 'Заметки'),
    ]
    # address

    shipping_address_line_1 = models.CharField(max_length=255, verbose_name='Адрес', default='Адрес не указан')
    shipping_address_line_2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес (дополнительный)')
    shipping_city = models.CharField(max_length=100, verbose_name='Город', default='Город не указан')
    shipping_postal_code = models.CharField(max_length=35, verbose_name='Почтовый код', default='Почтовый код не указан')
    shipping_country = models.CharField(max_length=100, verbose_name='Страна', default='Страна не указана')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    total_amount = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Кол-во')
    status = models.CharField(max_length=15, choices=ORDER_STATUS_CHOICES, default=DRAFT, verbose_name='Статус заказа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')

    def __str__(self):
        return f'Order ID: {self.pk}; total_amount: {self.total_amount}; status: {self.status}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.IntegerField(verbose_name='Кол-во')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')


