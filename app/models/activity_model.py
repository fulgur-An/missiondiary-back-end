from django.db import models
from app.models.user_model import User


class Activity(models.Model):
  user = models.ForeignKey(
    User, 
    on_delete=models.CASCADE,
  )
  description = models.TextField(max_length=500)
  start_date = models.DateTimeField(auto_now=True)
  end_date = models.DateTimeField()
  points = models.IntegerField()
  PriorityLevel = (
    ('NO','noUrgent'),
    ('UR','urgent'),
    ('EM','emergency'),
  )
  priority_level = models.CharField(blank=True, choices=PriorityLevel, max_length=30)
  ActivityState = (
    ('WH','whithoutStart'),
    ('PE','pending'),
    ('FA','failed'),
    ('CO','completed'),
  )
  state = models.CharField(blank=True, choices=ActivityState, max_length=30)
  title = models.CharField(max_length=100)
  ActivityType = (
    ('FA','family'),
    ('SI','single'),
  )
  type = models.CharField(blank=True, choices=ActivityType, max_length=30)

