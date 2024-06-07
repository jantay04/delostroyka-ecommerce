from django.urls import path

from .views import ClientRegistrationView, ClientLoginView, ClientLogoutView

urlpatterns = [
    path('register/client/', ClientRegistrationView.as_view(), name='register-client'),
    path('login/client/', ClientLoginView.as_view(), name='login-client'),
    path('logout/client/', ClientLogoutView.as_view(), name='logout-client'),
]