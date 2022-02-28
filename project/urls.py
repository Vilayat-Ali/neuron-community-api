from django.urls import path

from .views import *

urlpatterns = [
    path('', projectView.as_view()),
]