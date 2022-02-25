from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializer import *

class memberView(APIView):
    def get(self, request, *args, **kwargs):
        members = member.objects.all() 
        memberList = memberSerializer(members, many=True)
        return Response(memberList.data)
    def post(self, request, *args, **kwargs):
        return Response("Members")
