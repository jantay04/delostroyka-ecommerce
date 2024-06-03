from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from rest_framework import serializers, status
from rest_framework.response import Response

from user.models import CustomUser
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def validate(self, data):
        if CustomUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            is_client=True,
        )
        user.set_password(validated_data['password'])
        client = Client.objects.create(pk=user.pk,
            user=user, full_name=f'Гость {user.pk}',
        )
        return user


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id'] = instance.pk
        representation['full_name'] = Client.objects.get(user=instance).full_name
        representation.pop('password', None)
        return representation


