from django.contrib import admin
from django.urls import path, include 
from diary.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home",home, name="index"),
    path('write',postDiary),
    path('collection',mydiary),
    path('music',mood),
    path('', include('authentication.urls')),
]
