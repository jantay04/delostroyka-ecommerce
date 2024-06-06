from django.shortcuts import render
from rest_framework import viewsets

from .models import Provider
from .serializers import ProviderSerializer


# Create your views here.
class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
