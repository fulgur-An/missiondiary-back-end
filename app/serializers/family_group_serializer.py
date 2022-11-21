from app.models  import FamilyGroup 
from rest_framework import serializers

class FamilyGroupSerializer(serializers.Serializer):
  image = serializers.ImageField()
  name = serializers.CharField(max_length=100)
  quantity_members = serializers.IntegerField()

  def create(self, validate_data):
    return FamilyGroup.objects.create(**validate_data)

