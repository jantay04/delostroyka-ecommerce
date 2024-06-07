from django.db import models
from django.db.models import Avg
from autoslug import AutoSlugField

from api.user.models import CustomUser


class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product_images/', default='product_images/default-product/',
                              verbose_name='Картинка')

    def __str__(self):
        return f"Image for {self.product.name}"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=255, verbose_name='Описание')
    price = models.DecimalField(decimal_places=2, max_digits=8, verbose_name='цена за 1шт')
    quantity = models.IntegerField(verbose_name='Кол-во')
    feature = models.JSONField(verbose_name='Характеристики')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории', related_name='products')
    provider = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Поставщик')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')

    def __str__(self):
        return f'Product_name: {self.name}; price: {self.price}'

    def get_average_rating(self):
        average = self.reviews.aggregate(Avg('score'))['score__avg']
        if average is not None:
            return round(average, 2)
        return 0.0
