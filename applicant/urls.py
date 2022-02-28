from django.urls import path

from .views import *

urlpatterns = [
    path('', applicantView.as_view())
]
