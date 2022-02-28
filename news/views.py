from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *

class newsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            allNews = community_new.objects.all()
            newSerialized = newSerializer(allNews, many=True)

            return Response({
                'status': 'success',
                'data': newSerialized.data
            })
        except Exception as e:
            return Response({ 'status': 'failed', 'message': e.args})
