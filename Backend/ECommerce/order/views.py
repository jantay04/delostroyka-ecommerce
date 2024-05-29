from django.shortcuts import render
from rest_framework import viewsets

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer