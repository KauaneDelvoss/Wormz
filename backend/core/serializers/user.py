from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User as UserDjangoAuth

from core.models import User

class UserAuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    id = serializers.IntegerField()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"