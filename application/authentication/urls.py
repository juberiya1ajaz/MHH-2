from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
]
 # API Key: fEEm5Im9bGG0XzyQHnjWnCZb6m9jbz1JFFW5oEgl