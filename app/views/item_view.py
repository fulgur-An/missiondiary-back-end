from app.models import Item, ItemPlayer, Player
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json
from app.views.auth_view import Auth
from rest_framework.response import Response

class ItemView(APIView):
  def get(self, request, id=0):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      itemsPlayer=list(ItemPlayer.objects.values())
      data={'message':"items not found..."}
      if id > 0:
        try:
          item = Item.objects.get(pk=id)
        except:
          return Response(status=400)
          del item.__dict__['_state']
          data={'item':item.__dict__}
      else:
        try:
          items=list(Item.objects.values())
        except:
          Response(status=404)
        if len(items)>0:
          data={'items':items}
      return JsonResponse(data)
    else:
      return Response(status=401)

  def post(self, request):
    token = request.headers['Authorization']
    isAuthenticated = Auth.VerifyToken(token)
    if not isAuthenticated:
      return Response(status=401)
    
    user_id = Auth.GetTokenUserId(token)
    jd = json.loads(request.body)
    try:
      item=Item.objects.get(pk=jd['id'])
      player=Player.objects.get(pk=user_id)
    except:
      return Response(status=400)
    if item.__dict__['price'] <= player.__dict__['points']:
      try:
        player.__dict__['points']-=item.__dict__['price']
        ItemPlayer.objects.create(user_name=player.__dict__['user_name'],
        quantity=1,
        user=player,
        item=item,
        )
        player.save()
        data = {'message':'Success'}
        return Response(data)
      except:
        Response(status=400)
    else:
      return Response(status=404)
