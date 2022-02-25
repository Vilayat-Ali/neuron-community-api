from rest_framework.views import APIView
from rest_framework.response import Response

class homeView(APIView):
    def get(self, request, *args, **kwargs):
        responseObj = {
            'commodity': 'Community API',
            'version': '1.0.1v',
            'author': 'Syed Vilayat Ali Rizvi'
        }
        return Response(responseObj)