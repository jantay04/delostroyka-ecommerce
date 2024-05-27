from django.urls import path, include
from rest_framework import routers

from .views import UserManageViewSet, UserLoginView, UserLogoutView

router = routers.SimpleRouter()

router.register(r'users', UserManageViewSet, basename='users')


urlpatterns = [path('login/', UserLoginView.as_view(), name='login'),
               path('logout/', UserLogoutView.as_view(), name='logout'),
               path('', include(router.urls), name='users'),
               ]