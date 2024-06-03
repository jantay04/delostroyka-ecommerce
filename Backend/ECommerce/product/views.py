from django.shortcuts import render
from rest_framework import viewsets

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from drf_spectacular.utils import extend_schema

# Create your views here.



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer