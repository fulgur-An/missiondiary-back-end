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
          del player.__dict__['_state']
          del player.__dict__['password']
          data={'player':player.__dict__}
        except:
          return Response(status=400)
      else:
        players=list(Player.objects.values())
        for player in players:
          del player['password']
        if len(players)>0:
          data={'Players':players}
      return Response(data)
    else:
      return Response(status=401)

  def post(self, request):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      try:
        player = Player.objects.get(user_name=request.data.get("user_name"))
        del player.__dict__['_state']
        del player.__dict__['password']
        return Response(player.__dict__)
      except:
        return Response(status=400)
    else:
      return Response(status=401)

  def put(self, request, id):
    token = request.headers['Authorization']
    isAuthenticated = Auth.VerifyToken(token)
    user_id = Auth.GetTokenUserId(token)
    if isAuthenticated and user_id == id:
      jd = json.loads(request.body)
      try:
        if jd['name']=='' :
          return Response(status=400)
      except:
        return Response(status=400)
      try:
        player=Player.objects.get(pk=id)
        if jd['level'] > 0 :
          player.__dict__['level']+=1
          player.__dict__['points']+=jd['points']
        else:
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
      except:
        return Response(status=400)
    else:
      return Response(status=401)
    
