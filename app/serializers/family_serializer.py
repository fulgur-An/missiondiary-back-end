from app.models import Family 
from rest_framework import serializers


class FamilySerializer(serializers.Serializer):
  user = serializers.CharField(max_length=100)
  FamilyType = (
    ('FA','father'),
    ('MO','mother'),
    ('SI','sister'),
    ('BR','brother'),
    ('CH','child'),
    ('WI','wife'),
    ('HU','husband'),
  )
  type = serializers.ChoiceField(choices=FamilyType)
  user_name = serializers.CharField(max_length=100)

  def create(self, validate_data):
    return Family.objects.create(**validate_data)

