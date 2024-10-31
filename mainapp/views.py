from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import JsonFileUpload, dyFrmBuilder
import json

def homeView(request):
    return render(request, 'mainapp/home.html')



@login_required
def uploadJsonVeiw(request):
    if request.method=="POST":
        jsonFUfrm = JsonFileUpload(request.POST, request.FILES)
        jsonData = request.FILES.get('jsonFile')
        jsonData= jsonData.read().decode('UTF-8')
        try:
            data = json.loads(jsonData)
            dyFrm = dyFrmBuilder(data)

            dynamicFrom = dyFrm()
            return render(request, 'mainapp/upload.html', {'form': dynamicFrom, 'action':data["action"], 'jsonFUfrm':JsonFileUpload()})
        except:
            return HttpResponse("You have an error in json schema")

    else:
         jsonFUfrm = JsonFileUpload()
         return render(request , 'mainapp/upload.html', {'jsonFUfrm': jsonFUfrm })