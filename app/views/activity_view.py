from app.models import Activity
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json

class ActivityView(APIView):
  def get(self, request):
    activities=list(Activity.objects.values())
    if len(activities)>0:
      data={'message':"success",'activities':activities}
    else:
      data={'message':"activities not found..."}
    return JsonResponse(data)

  def post(self, request):
    jd = json.loads(request.body)
    Activity.objects.create(user=jd['user'],
    description=jd['description'],
    start_date=jd['start_date'],
    end_date=jd['end_date'],
    points=jd['points'],
    priority_level=jd['priority_level'],
    state=jd['state'],
    title=jd['title'],
    type=jd['type'],
    )
    data = {'message':'Success'}
    return JsonResponse(data)

  def put(self, request):
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

  def delete(self, request):
    activities=list(Activity.objects.filter(id=id).values())
    if len(activities) > 0:
      Activity.objects.filter(id=id).delete()
      data= {'message': 'Success'}
    else:
      data={'message':"users not found..."}
    return JsonResponse(data)

