from django.urls import path, include


from .views import UserCreateAPIView, UserLoginView, UserLogoutView


urlpatterns = [path('login/', UserLoginView.as_view(), name='login'),
               path('logout/', UserLogoutView.as_view(), name='logout'),
               path('add_user/', UserCreateAPIView.as_view(), name='add_user'),
               ]