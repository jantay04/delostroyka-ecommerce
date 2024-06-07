from config.settings import base
from django.db import models

from api.product.models import Product


# Create your models here.
class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        unique_together = [
            'user',
            'product']
    user = models.ForeignKey(
        base.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews')
    score = models.PositiveIntegerField(
        null=False,
        blank=False)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)