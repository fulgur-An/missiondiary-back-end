from django.urls import include, path


from app.views.player_view import PlayerView
from app.views.family_view import FamilyView
from app.views.item_view import ItemView
from app.views.item_player_view import ItemPlayerView
from app.views.activity_view import ActivityView
from app.views.register_view import RegisterView
from app.views.auth_view import Auth

urlpatterns = [
  path('users/', PlayerView.as_view(), name='user_list'),
  path('users/<int:id>', PlayerView.as_view(), name='user'),
  path('register/',RegisterView.as_view(), name='register'),
  path('login/', Auth.as_view(), name='user_login'),
  path('family/<int:id>', FamilyView.as_view(), name='family_list'),
  path('family/', FamilyView.as_view(), name='family'),
  path('item/<int:id>', ItemView.as_view(), name='item_list'),
  path('item/', ItemView.as_view(), name='item'),
  path('itemPlayer/', ItemPlayerView.as_view(), name='item_player_list'),
  path('activity/<int:id>', ActivityView.as_view(), name='activity_list'),
  path('activity/', ActivityView.as_view(), name='activity'),
]