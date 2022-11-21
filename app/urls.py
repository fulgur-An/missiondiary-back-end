

from django.urls import include, path

# from views import user_view, family_view, item_view, activity_view, auth_view

from app.views.user_view import UserView
from app.views.family_view import FamilyView
from app.views.item_view import ItemView
from app.views.activity_view import ActivityView
from app.views.auth_view import Auth

urlpatterns = [
  path('users/', UserView.as_view(), name='user_list'),
  path('users/<int:id>', UserView.as_view(), name='user'),
  path('login/', Auth.as_view(), name='user_login'),
  path('family/<int:id>', FamilyView.as_view(), name='family_list'),
  path('family/', FamilyView.as_view(), name='family'),
  path('item/<int:id>', ItemView.as_view(), name='item_list'),
  path('item/', ItemView.as_view(), name='item'),
  path('activity/<int:id>', ActivityView.as_view(), name='activity_list'),
  path('activity/', ActivityView.as_view(), name='activity'),
  # path('o/',include('oauth2_provider.urls', namespace='oauth2_provider'))
]