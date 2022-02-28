from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *

class applicantView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            applicantModel = applicant.objects.all()
            applicantResponse = applicantSerializer(applicantModel)
            response = { 'status': 'success', 'data': applicantResponse.data}
            return Response(response)
        except Exception as e:
            return Response ({'status': 'error', 'message': e.args})

    def post(self, request, *args, **kwargs):
        try:
            applicantInstance = applicant(
                full_name = request.data['full_name'],
                email = request.data['email'],
                phone = request.data['phone'],
                description = request.data['description']
            )

            applicantInstance.save()

            return Response({
                'status': 'success',
                'message': 'requested for joining successfully...'
            })
            
        except Exception as e:
            return Response({
                'status': 'failed',
                'message': e.args
            })

