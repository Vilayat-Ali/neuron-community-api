from rest_framework.views import APIView
from rest_framework.response import Response 

from .models import *
from .serializer import *

class projectView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            projects = project.objects.all()
            serializedProjects = projectSerializer(projects, many=True)
            return Response({
                'status': 'success',
                'data': serializedProjects.data
            })
        except Exception as e:
            return Response({
                'status': 'failed',
                'message': e.args
            })
