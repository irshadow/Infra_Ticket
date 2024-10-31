from django.urls import path
from . import  views
from mainapp.views import homeView
urlpatterns =[
    path('', views.index, name= "index"),
    path('login/', views.doLogin, name= "login"),
    path('logout/', views.logoutView, name="logout")
]

