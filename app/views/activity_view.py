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
      state='active',
      title=jd['title'],
      type=jd['type'],
      )
      data = {'message':'Success'}
      return JsonResponse(data)
    else:
      return Response(status=401)

  def put(self, request, id):
    token = request.headers['Authorization']
    isAuthenticated = Auth.VerifyToken(token)
    if isAuthenticated:
      user_id = Auth.GetTokenUserId(token)
      jd = json.loads(request.body)
      try:
        activity=Activity.objects.get(pk=id)
        if activity.__dict__['user_id']==user_id:
          points = 0
          if jd['priority_level'] == 'High':
            points = 50
          elif jd['priority_level'] == 'Meddium':
            points = 30
          elif jd['priority_level'] == 'Low':
            points = 10
          else:
            points = 0

          if jd['state'] == 'done':
            activity.__dict__['state']=jd['state']
          else:
            activity.__dict__['description']=jd['description']
            activity.__dict__['start_date']=jd['start_date']
            activity.__dict__['end_date']=jd['end_date']
            activity.__dict__['points']=points
            activity.__dict__['priority_level']=jd['priority_level']
            activity.__dict__['state']='active'
            activity.__dict__['title']=jd['title']
            activity.__dict__['type']=jd['type']
          
          
          activity.save()
          del activity.__dict__['_state']
          data= {'activity': activity.__dict__}
          response = Response(data)
      except Exception as e:
        print(e)
        response = Response(status=404)
      
      return response
    else:
      return Response(status=401)

  def delete(self, request, id):
    token = request.headers['Authorization']
    isAuthenticated = Auth.VerifyToken(token)
    user_id = Auth.GetTokenUserId(token)
    if isAuthenticated:
      try:
        activity=Activity.objects.get(pk=id)
        if activity.__dict__['user_id']==user_id:
          activity.__dict__['state']='ended'
          activity.save()
          del activity.__dict__['_state']
          data= {'activity': activity.__dict__}
          response = Response(data)
      except Exception as e:
        print(e)
        response = Response(status=404)
      return response
    else:
      return Response(status=401)

