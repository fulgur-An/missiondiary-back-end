from models.item_model import Item 
from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
  item_name = serializers.CharField(max_length=100)
  image = serializers.ImageField()
  price = serializers.IntegerField()
  description = serializers.CharField(max_length=500)

  def create(self, validate_data):
    return Item.objects.create(**validate_data)

