from django.db import models

from provider.models import Provider


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=255, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='product_images/', default='product_images/default-product/', verbose_name='Картинка')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=255, verbose_name='Описание')
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='цена за 1шт')
    quantity = models.IntegerField(verbose_name='Кол-во')
    feature = models.JSONField(verbose_name='Характеристики')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Поставщик')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')

    def __str__(self):
        return f'Product_name: {self.name}; price: {self.price}'
