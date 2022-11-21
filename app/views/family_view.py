
from app.models import Family
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json



class FamilyView(APIView):

  def get(self, request):
    families=list(Family.objects.values())
    if len(families)>0:
      data={'message':"success",'families':families}
    else:
      data={'message':"families not found..."}
    return JsonResponse(data)

  def post(self, request):
    jd = json.loads(request.body)
    Family.objects.create(user=jd['user'],
    type=jd['type'],
    user_name=jd['user_name'])
    data = {'message':'Success'}
    return JsonResponse(data)
    
  def put(self, request):
    jd = json.loads(request.body)
    famlilies=list(Family.objects.filter(id=id).values())
    if len(famlilies) > 0:
      family=Family.objects.get(id=id)
      family.user=jd['user']
      family.type=jd['type']
      family.user_name=jd['user_name']
      data= {'message': 'Success'}
    else:
      data={'message':"users not found..."}
    return JsonResponse(data)

  def delete(self, request):
    families=list(Family.objects.filter(id=id).values())
    if len(families) > 0:
      Family.objects.filter(id=id).delete()
      data= {'message': 'Success'}
    else:
      data={'message':"users not found..."}
    return JsonResponse(data)