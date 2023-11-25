from rest_framework import serializers
from .models import User
from .services import UserService

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']

    def create(self, validated_data):
        service = UserService()
        return service.create_user(**validated_data)