import base64
from app.models import Player
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from app.serializers.player_serializer import PlayerSerializer
import bcrypt, hashlib
from jose import jwt
from datetime import datetime, date, timedelta
import environ

class RegisterView(APIView):
  permission_classes = [AllowAny]
  serializer_class = PlayerSerializer
  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    request_data = request.data
    isValid = True
    try:
      Player.objects.get(pk=request.data.get("user_name"))
    except:
      isValid = False

    if not isValid:
      if serializer.is_valid():
        raw_password = request_data['password'].encode()
        password_hash = bcrypt.hashpw(base64.b64encode(hashlib.sha256(raw_password).digest()), bcrypt.gensalt()).decode()
        Player.objects.create(user_name=request_data['user_name'],
          mail=request_data['mail'],
          password=password_hash,
          name=request_data['name'],
          last_name=request_data['last_name'],
        )
        now = str(datetime.now())
        expired = str(datetime.now() + timedelta(minutes=15))
        keys = {
          'player': request.data.get("user_name"),
          'date': now,
          'expiration_date': expired
        }
        env = environ.Env()
        environ.Env.read_env()
        token = jwt.encode(
          keys,
          env("SECRET_KEY"),
          algorithm='HS256')
        return Response(token, status=status.HTTP_200_OK)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    else:
      return Response(status=status.HTTP_200_OK)
    # 
