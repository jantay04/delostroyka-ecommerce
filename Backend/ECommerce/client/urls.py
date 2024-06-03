from django.urls import path
from .views import ClientCreateView, ClientLogoutView

urlpatterns = [
    path('register/client/', ClientCreateView.as_view(), name='client-register'),
    path('logout/client/', ClientLogoutView.as_view(), name='client-logout'),
]