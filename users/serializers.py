from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import NewUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('id', 'email', 'user_name', 'first_name', 'last_name')
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['user_name'] = user.user_name
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        return token

class EditUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = NewUser
        fields = ('id', 'email', 'user_name', 'first_name', 'last_name', 'password', 'confirm_password')

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords must match")
        return data

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance
