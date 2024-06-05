from rest_framework import serializers

from .models import CustomUser


class ClientRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=128)

    class Meta:
        model = CustomUser
        fields = ('email', 'password',)

    def validate(self, data):
        email_exist = CustomUser.objects.filter(username=data['email']).exists()
        if email_exist:
            raise serializers.ValidationError('Пользователь с такой почтой уже существует')
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data,
                          is_client=True)
        user.full_name = 'Гость ' + str(user.pk)
        user.save()
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id'] = instance.id
        representation['full_name'] = instance.full_name
        representation.pop('password', None)
        return representation


class ClientLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=128)

    class Meta:
        model = CustomUser
        fields = ('email', 'password',)