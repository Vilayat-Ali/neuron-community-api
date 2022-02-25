from django.urls import path

from .views import *

urlpatterns = [
    path('', memberView.as_view())
]
