
from app.models import User
from rest_framework.views import APIView, exception_handler
from rest_framework.response import Response
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import BasePermission, SAFE_METHODS, AllowAny
from django.utils.decorators import method_decorator
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.authtoken.models import Token
from django.http.response import JsonResponse
from app.serializers.user_serializer import UserSerializer
import json
from jose import jwt
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, date, timedelta

import environ



class Auth(APIView):
  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)
  permission_classes = [AllowAny]
  def post(self, request):
    try:
      queryset = User.objects.get(pk=request.data.get("user_name"))
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)
    raw_password = request_data['password'].encode('utf_8')
    password_hash = bcrypt.hashpw(base64.b64encode(hashlib.sha256(raw_password).digest()), bcrypt.gensalt(rounds=12, prefix=b"2a"))
    original_password = queryset.data.get("password")
    if raw_password == original_password:
      now = str(datetime.now())
      expired = str(datetime.now() + timedelta(minutes=15))
      keys = {
        'player': request.data.get("user_name"),
        'date': now,
        'expiration_date': expired
      }
      env = environ.Env()
      environ.Env.read_env()
      if queryset.user_name == request.data.get("user_name") and queryset.password == request.data.get("password"):
        token = jwt.encode(
          keys,
          env("SECRET_KEY"),
          algorithm='HS256')
        return Response(data=token,status=status.HTTP_200_OK)
      return Response(status=status.HTTP_404_NOT_FOUND)
    else:
      return Response(status=404)
  def VerifyToken(token):
    try:
      env = environ.Env()
      environ.Env.read_env()
      # key = 
      data = jwt.decode(token, env("SECRET_KEY"), algorithms=['HS256'])
      player = data['player']
      expired = data['expiration_date']
      # if 
      # user
      try:
        user = User.objects.get(pk=player)
      except:
        user = False
      now = str(datetime.now())
      if user != False and now < expired:
        return True
      else:
        return False
    except jwt.JWTError:
      return False

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

