from app.models  import Activity 
from rest_framework import serializers

class ActivitySerializer(serializers.Serializer):
  user = serializers.CharField(max_length=100)
  description = serializers.CharField(max_length=500)
  start_date = serializers.DateTimeField()
  end_date = serializers.DateTimeField()
  points = serializers.IntegerField()
  PriorityLevel = (
    ('NO','noUrgent'),
    ('UR','urgent'),
    ('EM','emergency'),
  )
  priority_level = serializers.ChoiceField(choices=PriorityLevel)
  ActivityState = (
    ('WH','whithoutStart'),
    ('PE','pending'),
    ('FA','failed'),
    ('CO','completed'),
  )
  state = serializers.ChoiceField(choices=ActivityState)
  title = serializers.CharField(max_length=100)
  ActivityType = (
    ('FA','family'),
    ('SI','single'),
  )
  type = serializers.ChoiceField(choices=ActivityType)

  def create(self, validate_data):
    return Activity.objects.create(**validate_data)