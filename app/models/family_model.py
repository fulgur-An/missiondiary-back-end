from django.db import models
from app.models.user_model import User



class Family(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  FamilyType = (
    ('FA','father'),
    ('MO','mother'),
    ('SI','sister'),
    ('BR','brother'),
    ('CH','child'),
    ('WI','wife'),
    ('HU','husband'),
  )
  type = models.CharField(blank=True, choices=FamilyType, max_length=30)
  user_name = models.CharField(max_length=100)
