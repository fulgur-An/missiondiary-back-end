from django.db import models


class FamilyGroup(models.Model):
  image = models.ImageField()
  name = models.CharField(max_length=100)
  quantity_members = models.IntegerField()