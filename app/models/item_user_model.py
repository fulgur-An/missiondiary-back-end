from django.db import models
from app.models.user_model import User
from app.models.item_model import Item

class ItemUser(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  user_name = models.CharField(max_length=100)