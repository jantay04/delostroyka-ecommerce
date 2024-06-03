from collections import OrderedDict

from django.contrib.auth import authenticate, login, logout
from rest_framework import views, generics, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from user.models import CustomUser
from .models import Client
from .serializers import ClientSerializer


class ClientCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ClientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user)
        # Authenticate and log in the user
        if user is not None:
            login(request, user)

        return Response({
            'user': serializer.data,
            'email': user.email,
            'message': 'User registered and logged in successfully.'
        }, status=status.HTTP_201_CREATED)


class ClientLogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'detail': 'User succesfully logged out'}, status=status.HTTP_200_OK)

