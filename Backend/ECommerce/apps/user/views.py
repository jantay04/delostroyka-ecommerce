from django.contrib.auth import login, logout, authenticate
from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser
from .serializers import ClientRegisterSerializer


class ClientRegistrationView(generics.CreateAPIView):
    serializer_class = ClientRegisterSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        login(request, user)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ClientLoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(username=email, email=email, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Такой пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Не удалось войти.'}, status=status.HTTP_401_UNAUTHORIZED)


class ClientLogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data, status=status.HTTP_200_OK)