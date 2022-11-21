from django.db import models
from app.models.family_group_model import FamilyGroup
from app.models.item_model import Item
# from app.auth_model import AuthModel

class User(models.Model):
  # auth = models.OneToOneField(
  #   AuthModel,
  #   on_delete=models.CASCADE,
  #   verbose_name="related auth")
  family_group = models.ForeignKey(
    FamilyGroup,
    null= True,
    on_delete=models.SET_NULL,
  )
  items = models.ManyToManyField(Item)
  user_name = models.CharField(primary_key=True, max_length=100)
  mail = models.EmailField(max_length=100)
  password = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  avatar = models.ImageField()

class AuthToken(models.Model):
  user_name = models.CharField(primary_key=True, max_length=100)
  password = models.CharField(max_length=100)
  token = models.CharField(max_length=100)

