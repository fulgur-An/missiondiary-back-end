
from app.models import Player
from rest_framework import serializers

class PlayerSerializer(serializers.Serializer):
  user_name = serializers.CharField(read_only = True, max_length=100)
  mail = serializers.EmailField(max_length=100)
  password = serializers.CharField(max_length=100)
  name = serializers.CharField(max_length=100)
  last_name = serializers.CharField(max_length=100)

  def create(self, validate_data):
    return Player.objects.create(**validate_data)
  # def update():



