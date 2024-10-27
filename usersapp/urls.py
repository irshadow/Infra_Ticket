from django.urls import path
from . import  views
from mainapp.views import homeView
urlpatterns = [
    path('', views.index),
    path('login/', views.doLogin),
    path('logout/', views.logoutView)
]

