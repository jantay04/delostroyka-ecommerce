from rest_framework import viewsets, filters as filter_search
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters
from .models import Product, Category, ProductImage
from .serializers import ProductSerializer, CategorySerializer, ProductImageSerializer


# Create your views here.
class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filter_search.SearchFilter]
    filterset_class = ProductFilter


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [AllowAny]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


