from django.db import models

from account.models import CustomUser
from product.models import Product


# Create your models here.
class Order(models.Model):
    PENDING_PAYMENT = 'pending_payment'
    PROCESSING = 'processing'
    ON_HOLD = 'on_hold'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    REFUNDED = 'refunded'
    FAILED = 'failed'
    DRAFT = 'draft'

    ORDER_STATUS_CHOICES = [
        (PENDING_PAYMENT, 'Pending Payment'),
        (PROCESSING, 'Processing'),
        (ON_HOLD, 'On Hold'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
        (REFUNDED, 'Refunded'),
        (FAILED, 'Failed'),
        (DRAFT, 'Draft'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, default=DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order ID: {self.pk}; total_amount: {self.total_amount}; status: {self.status}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


