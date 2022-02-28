from django.urls import path

from .views import *

urlpatterns = [
    path('', newsView.as_view()),
]