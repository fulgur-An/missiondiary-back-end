
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
    now = str(datetime.now())
    expired = str(datetime.now() + timedelta(minutes=15))
    print(now)
    print(expired)
    keys = {
      'player': request.data.get("user_name"),
      'date': now,
      'expiration_date': expired
    }
    if queryset.user_name == request.data.get("user_name") and queryset.password == request.data.get("password"):
      token = jwt.encode(
        keys,
        'a!zLCLRvyQ%sc!rGhTW9z@CU9JU)bxv!nMtJ6E*g*$*%7I*5GF82s@2TH+cGq9%BnNJP(wEhy4HsRus2xXaJ%xcDMyL597', 
        algorithm='HS256')
      return Response(data={token},status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)




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

