from django.db import models


class Item(models.Model):
  item_name = models.CharField(max_length=100)
  image = models.ImageField()
  price = models.IntegerField()
  description = models.TextField(max_length=500)