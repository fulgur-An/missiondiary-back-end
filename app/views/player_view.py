from app.models import Player
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from app.serializers.player_serializer import PlayerSerializer
from app.views.auth_view import Auth
class PlayerView(APIView):
  serializer_class = PlayerSerializer
  def get(self, request, id=0):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      data={'message':"Players not found..."}
      if (id>0):
        try:
          player=Player.objects.get(pk=id)
        except:
          return Response(status=404)
        del player.__dict__['_state']
        del player.__dict__['password']
        data={'player':player.__dict__}
      else:
        players=list(Player.objects.values())
        if len(players)>0:
          data={'Players':players}
      return Response(data)
    else:
      return Response(status=401)

  def post(self, request):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      try:
        player = Player.objects.get(pk=request.data.get("user_name"))
      except:
        return Response(status=404)
      del player.__dict__['_state']
      del player.__dict__['password']
      return Response(player.__dict__)
    else:
      return Response(status=401)

  def put(self, request, id):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      jd = json.loads(request.body)
      try:
        player=Player.objects.get(pk=id)
      except:
        return Response(status=404)
      if jd['level'] > 0 :
        player.__dict__['level']+=1
        player.__dict__['points']+=jd['points']
      else:
        player.__dict__['user_name']=jd['user_name']
        player.__dict__['mail']=jd['mail']
        player.__dict__['name']=jd['name']
        player.__dict__['last_name']=jd['last_name']
        player.__dict__['avatar']=jd['avatar']
        player.__dict__['banner']=jd['banner']
      player.save()
      del player.__dict__['banner']
      del player.__dict__['avatar']
      del player.__dict__['password']
      del player.__dict__['_state']
      data= {'player': player.__dict__}
      return Response(data)
    else:
      return Response(status=401)
    
