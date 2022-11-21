from app.models  import ItemUser 
from rest_framework import serializers


class ItemUserSerializer(serializers.Serializer):
  user = serializers.CharField(max_length=100)
  item = serializers.CharField(max_length=100)
  quantity = serializers.IntegerField()
  user_name = serializers.CharField(max_length=100)

  def create(self, validate_data):
    return ItemUser.objects.create(**validate_data)


