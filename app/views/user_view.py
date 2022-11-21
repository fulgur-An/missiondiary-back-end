from app.models import User
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from app.serializers.user_serializer import UserSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class UserView(APIView):
  # permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
  serializer_class = UserSerializer
  
  def get(self, request, id=0):
    data={'message':"users not found..."}
    if (id>0):
      users=list(User.objects.values())
      if len(users) > 0:
        user=users[id - 1]
        data={'users':user}
    else:
      users=list(User.objects.values())
      if len(users)>0:
        data={'message':"success",'users':users}
    return JsonResponse(data)

  
  def post(self, request):

    serializer = self.serializer_class(data=request.data)
    data=Response(
      serializer.errors,
      status=status.HTTP_400_BAD_REQUEST)
    if serializer.is_valid():
      jd = json.loads(request.body)
      User.objects.create(family_group=jd['family_group'],
      items=jd['items'],
      user_name=jd['user_name'],
      mail=jd['mail'],
      password=jd['password'],
      name=jd['name'],
      last_name=jd['last_name'],
      avatar=jd['avatar'],
      )
      data = {'message':'Success'}
    return JsonResponse(data)

  def put(self, request):
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
    
  def delete(self, request, id):
    users=list(User.objects.filter(id=id).values())
    if len(users) > 0:
      User.objects.filter(id=id).delete()
      data= {'message': 'Success'}
    else:
      data={'message':"users not found..."}
    return JsonResponse(data)

