from django.urls import path
from .views import uploadJsonVeiw

urlpatterns = [
    path('uploadjason', uploadJsonVeiw, name= "uploadJson")
]
