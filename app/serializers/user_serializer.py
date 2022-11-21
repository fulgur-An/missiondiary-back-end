
from app.models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
  user_name = serializers.CharField(max_length=100)
  mail = serializers.EmailField(max_length=100)
  password = serializers.CharField(max_length=100)
  name = serializers.CharField(max_length=100)
  last_name = serializers.CharField(max_length=100)
  avatar = serializers.ImageField()

  def create(self, validate_data):
    return User.objects.create(**validate_data)


