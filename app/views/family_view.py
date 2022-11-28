
from app.models import Family
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json
from app.views.auth_view import Auth
from rest_framework.response import Response


class FamilyView(APIView):

  def get(self, request):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      families=list(Family.objects.values())
      if len(families)>0:
        data={'message':"success",'families':families}
      else:
        data={'message':"families not found..."}
      return JsonResponse(data)
    else:
      return Response(status=401)

  def post(self, request):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      jd = json.loads(request.body)
      Family.objects.create(user=jd['user'],
      type=jd['type'],
      user_name=jd['user_name'])
      data = {'message':'Success'}
      return JsonResponse(data)
    else:
      return Response(status=401)
    
  def put(self, request):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
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
    else:
      return Response(status=401)

  def delete(self, request):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      families=list(Family.objects.filter(id=id).values())
      if len(families) > 0:
        Family.objects.filter(id=id).delete()
        data= {'message': 'Success'}
      else:
        data={'message':"users not found..."}
      return JsonResponse(data)
    else:
      return Response(status=401)