
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "telegram", "first_name", "last_name"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "telegram", "password", "first_name", "last_name"]


class MessageSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=200)
