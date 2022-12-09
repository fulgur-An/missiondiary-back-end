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
          return Response(status=404)
          del item.__dict__['_state']
          data={'item':item.__dict__}
      else:
        items=list(Item.objects.values())
        if len(items)>0:
          data={'items':items}
      return JsonResponse(data)
    else:
      return Response(status=401)

  def post(self, request):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if not isAuthenticated:
      return Response(status=401)
    
    user_id = Auth.GetTokenUserId(token)
    jd = json.loads(request.body)
    try:
      item=Item.objects.get(pk=jd['id'])
      player=Player.objects.get(pk=user_id)
    except:
      return Response(status=404)
    if item.__dict__['price'] <= player.__dict__['points']:
      player.__dict__['points']-=item.__dict__['price']
      ItemPlayer.objects.create(user_name=player.__dict__['user_name'],
      quantity=1,
      user=user_id,
      item=item.__dict__['id'],
      )
      data = {'message':'Success'}
      return Response(data)
    else:
      return Response(status=404)

  # def put(self, request):
  #   isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
  #   if isAuthenticated:
  #     jd = json.loads(request.body)
  #     items=list(Item.objects.filter(id=id).values())
  #     if len(items) > 0:
  #       item=Item.objects.get(id=id)
  #       item.item_name=jd['item_name']
  #       item.image=jd['image']
  #       item.price=jd['price']
  #       item.description=jd['description']
  #       data= {'message': 'Success'}
  #     else:
  #       data={'message':"users not found..."}
  #     return JsonResponse(data)
  #   else:
  #     return Response(status=401)

  # def delete(self, request):

  #   isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
  #   if isAuthenticated:
  #     items=list(Item.objects.filter(id=id).values())
  #     if len(items) > 0:
  #       Item.objects.filter(id=id).delete()
  #       data= {'message': 'Success'}
  #     else:
  #       data={'message':"users not found..."}
  #     return JsonResponse(data)
  #   else:
  #     return Response(status=401)
