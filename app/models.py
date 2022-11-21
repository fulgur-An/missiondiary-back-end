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


class ItemUser(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  user_name = models.CharField(max_length=100)

