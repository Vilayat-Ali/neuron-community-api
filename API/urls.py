from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', homeView.as_view()),
    path('api/member/', include('member.urls'))
]
