from app.models import ItemPlayer
from rest_framework.views import APIView
from django.http.response import JsonResponse
import json
from app.views.auth_view import Auth
from rest_framework.response import Response

class ItemPlayerView(APIView):
  def get(self, request):
    token = request.headers['Authorization']
    isAuthenticated = Auth.VerifyToken(token)
    if isAuthenticated:
      try:
        user_id = Auth.GetTokenUserId(token)
        itemsPlayer = list(ItemPlayer.objects.filter(user_id=user_id).values())
        if len(itemsPlayer)>0:
          data={'items':itemsPlayer}
        return Response(data)
      except:
        return Response(status=404)
    else:
      return Response(status=401)
