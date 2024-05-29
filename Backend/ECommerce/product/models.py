from django.db import models

from provider.models import Provider


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to='product_images/', default='product_images/default-product/')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    quantity = models.IntegerField()
    feature = models.JSONField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Product_name: {self.name}; price: {self.price}'
