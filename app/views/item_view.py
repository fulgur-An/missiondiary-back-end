from app.models import Item
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json


class ItemView(APIView):
  def get(self, request):
    items=list(Item.objects.values())
    if len(items)>0:
      data={'message':"success",'items':items}
    else:
      data={'message':"items not found..."}
    return JsonResponse(data)

  def post(self, request):
    jd = json.loads(request.body)
    Item.objects.create(item_name=jd['item_name'],
    image=jd['image'],
    price=jd['price'],
    description=jd['description'],
    )
    data = {'message':'Success'}
    return JsonResponse(data)

  def put(self, request):
    jd = json.loads(request.body)
    items=list(Item.objects.filter(id=id).values())
    if len(items) > 0:
      item=Item.objects.get(id=id)
      item.item_name=jd['item_name']
      item.image=jd['image']
      item.price=jd['price']
      item.description=jd['description']
      data= {'message': 'Success'}
    else:
      data={'message':"users not found..."}
    return JsonResponse(data)

  def delete(self, request):
    items=list(Item.objects.filter(id=id).values())
    if len(items) > 0:
      Item.objects.filter(id=id).delete()
      data= {'message': 'Success'}
    else:
      data={'message':"users not found..."}
    return JsonResponse(data)
