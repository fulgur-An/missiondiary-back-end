from app.models import User
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from app.serializers.user_serializer import UserSerializer
from app.views.auth_view import Auth
class UserView(APIView):
  serializer_class = UserSerializer
  def get(self, request, id=0):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      data={'message':"users not found..."}
      if (id>0):
        users=list(User.objects.values())
        if len(users) > 0:
          user=users[id - 1]
          user['password'] = ''
          data={'users':user}
      else:
        users=list(User.objects.values())
        if len(users)>0:
          data={'message':"success",'users':users}
      return JsonResponse(data)
    else:
      return Response(status=401)


  def put(self, request, id):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      jd = json.loads(request.body)
      users=list(User.objects.filter(id=id).values())
      if len(users) > 0:
        user=User.objects.get(id=id)
        user.family_group=jd['family_group']
        user.items=jd['items']
        user.user_name=jd['user_name']
        user.mail=jd['mail']
        user.password=jd['password']
        user.name=jd['name']
        user.last_name=jd['last_name']
        user.avatar=jd['avatar']
        data= {'message': 'Success'}
      else:
        data={'message':"users not found..."}
      return JsonResponse(data)
    else:
      return Response(status=401)
    
  def delete(self, request, id):

    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      users=list(User.objects.filter(id=id).values())
      if len(users) > 0:
        User.objects.filter(id=id).delete()
        data= {'message': 'Success'}
      else:
        data={'message':"users not found..."}
      return JsonResponse(data)
    else:
      return Response(status=401)


