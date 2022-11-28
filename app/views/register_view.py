import base64
from app.models import User
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from app.serializers.user_serializer import UserSerializer
import bcrypt, hashlib
from jose import jwt
from datetime import datetime, date, timedelta


class RegisterView(APIView):
  permission_classes = [AllowAny]
  serializer_class = UserSerializer
  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    # print(serializer)
    request_data = request.data
    isValid = True
    try:
      queryset = User.objects.get(pk=request.data.get("user_name"))
    except:
      isValid = False

    if not isValid:
      if serializer.is_valid():
        # jd = json.loads(request.data)     
        raw_password = request_data['password'].encode('utf_8')
        password_hash = bcrypt.hashpw(base64.b64encode(hashlib.sha256(raw_password).digest()), bcrypt.gensalt(rounds=12, prefix=b"2a"))
        User.objects.create(user_name=request_data['user_name'],
          mail=request_data['mail'],
          password=password_hash,
          name=request_data['name'],
          last_name=request_data['last_name'],
        )
        # data = {'message':'Success'}
        now = str(datetime.now())
        expired = str(datetime.now() + timedelta(minutes=15))
        keys = {
          'player': request.data.get("user_name"),
          'date': now,
          'expiration_date': expired
        }
        token = jwt.encode(
          keys,
          'a!zLCLRvyQ%sc!rGhTW9z@CU9JU)bxv!nMtJ6E*g*$*%7I*5GF82s@2TH+cGq9%BnNJP(wEhy4HsRus2xXaJ%xcDMyL597', 
          algorithm='HS256')
        return JsonResponse({'token': token}, status=status.HTTP_200_OK)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    else:
      return Response(status=status.HTTP_200_OK)
    # 
