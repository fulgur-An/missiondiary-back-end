from app.models import Activity
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json
from app.views.auth_view import Auth
from rest_framework.response import Response

class ActivityView(APIView):
  def get(self, request):
    token = request.headers['Authorization']
    isAuthenticated = Auth.VerifyToken(token)
    id_player = Auth.GetTokenUserId(token)
    # print(id_player)
    if isAuthenticated and id_player != 0:
      activities=list(Activity.objects.filter(user_id=id_player).values())
      if len(activities)>0:
        data={'activities':activities}
      else:
        data={'message':"activities not found..."}
      return JsonResponse(data)
    else:
      return Response(status=401)

  def post(self, request):
    token = request.headers['Authorization']
    isAuthenticated = Auth.VerifyToken(token)
    if isAuthenticated:
      user_id = Auth.GetTokenUserId(token)
      jd = json.loads(request.body)
      points = 0
      if jd['priority_level'] == 'High':
        points = 50
      elif jd['priority_level'] == 'Meddium':
        points = 30
      elif jd['priority_level'] == 'Low':
        points = 10
      else:
        points = 0
      Activity.objects.create(user_id=user_id,
      description=jd['description'],
      start_date=jd['start_date'],
      end_date=jd['end_date'],
      points=points,
      priority_level=jd['priority_level'],
      state='active ',
      title=jd['title'],
      type=jd['type'],
      )
      data = {'message':'Success'}
      return JsonResponse(data)
    else:
      return Response(status=401)

  def put(self, request):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      jd = json.loads(request.body)
      activities=list(Activity.objects.filter(id=id).values())
      if len(activities) > 0:
        activity=Activity.objects.get(id=id)
        activity.user=jd['user']
        activity.description=jd['description']
        activity.start_date=jd['start_date']
        activity.end_date=jd['end_date']
        activity.points=jd['points']
        activity.priority_level=jd['priority_level']
        activity.state=jd['state']
        activity.title=jd['title']
        activity.type=jd['type']
        data= {'message': 'Success'}
      else:
        data={'message':"users not found..."}
      return JsonResponse(data)
    else:
      return Response(status=401)

  def delete(self, request):
    isAuthenticated = Auth.VerifyToken(request.headers['Authorization'])
    if isAuthenticated:
      activities=list(Activity.objects.filter(id=id).values())
      if len(activities) > 0:
        Activity.objects.filter(id=id).delete()
        data= {'message': 'Success'}
      else:
        data={'message':"users not found..."}
      return JsonResponse(data)
    else:
      return Response(status=401)

