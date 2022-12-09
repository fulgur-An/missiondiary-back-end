from django.db import models



class FamilyGroup(models.Model):
  image = models.ImageField()
  name = models.CharField(max_length=100)
  quantity_members = models.IntegerField()



class Item(models.Model):
  item_name = models.CharField(max_length=100)
  image = models.ImageField()
  price = models.IntegerField()
  description = models.TextField(max_length=500)


class Player(models.Model):
  family_group = models.ForeignKey(
    FamilyGroup,
    null= True,blank=True,
    on_delete=models.SET_NULL, default=''
  )
  items = models.ManyToManyField(Item, null=True)
  points = models.IntegerField(default=0)
  user_name = models.CharField(unique=True, max_length=100)
  mail = models.EmailField(max_length=100, unique=True)
  password = models.CharField(max_length=100)
  name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  avatar = models.ImageField(null=True)


  

class Family(models.Model):
  user = models.ForeignKey(Player, on_delete=models.CASCADE)
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



class Activity(models.Model):
  user = models.ForeignKey(
    Player, 
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


class ItemPlayer(models.Model):
  user = models.ForeignKey(Player, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  user_name = models.CharField(max_length=100)


