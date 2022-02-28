from rest_framework.decorators import api_view
from rest_framework.response import Response

from newsletter.serializer import *

from .models import *

@api_view(['POST'])
def handleNewsletter(request, *args, **kwargs):
    newsLetterInstance = newsletter(email=request.data["email"])
    newsLetterInstance.save()
    return Response({ "status": "success", "message": "Newsletter subscribed!"})
