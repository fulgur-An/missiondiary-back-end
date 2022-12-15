
from app.models import Player
from rest_framework.views import APIView, exception_handler
from rest_framework.response import Response
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import BasePermission, SAFE_METHODS, AllowAny
from django.utils.decorators import method_decorator
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.authtoken.models import Token
from django.http.response import JsonResponse
from app.serializers.player_serializer import PlayerSerializer
import json
from jose import jwt
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, date, timedelta
import bcrypt, hashlib
import base64
import environ



class Auth(APIView):
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
  permission_classes = [AllowAny]
  def post(self, request):
    try:
      player = Player.objects.get(user_name=request.data.get("user_name"))
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)
    raw_password = request.data['password'].encode()
    original_password = player.password
    origin = original_password.encode()
    passwd = bcrypt.checkpw(base64.b64encode(hashlib.sha256(raw_password).digest()), origin)
    
    now = str(datetime.now())
    expired = str(datetime.now() + timedelta(minutes=15))
    keys = {
      'player': request.data.get("user_name"),
      'id_player': player.id,
      'date': now,
      'expiration_date': expired
    }
    env = environ.Env()
    environ.Env.read_env()
    if player.user_name == request.data.get("user_name") and passwd:
      token = jwt.encode(
        keys,
        env("SECRET_KEY"),
        algorithm='HS256')
      return Response({"token":token,"id":player.id},status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)
  def VerifyToken(token):
    try:
      env = environ.Env()
      environ.Env.read_env()
      data = jwt.decode(token, env("SECRET_KEY"), algorithms=['HS256'])
      player = data['id_player']
      expired = data['expiration_date']
      try:
        player = Player.objects.get(pk=player)
      except:
        player = False
      now = str(datetime.now())
      if Player != False and now < expired:
        return True
      else:
        return False
    except jwt.JWTError:
      return False
  def GetTokenUserId(token):
    try:
      env = environ.Env()
      environ.Env.read_env()
      data = jwt.decode(token, env("SECRET_KEY"), algorithms=['HS256'])
      player = data['id_player']
      return player
    except:
      return 0

  def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
      response.data['status_code'] = response.status_code

    return response

class ReadOnly(BasePermission):
  def has_permission(self, request, view):
    return request.method in SAFE_METHODS

