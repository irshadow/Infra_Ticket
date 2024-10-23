from django.shortcuts import render
import json
from pathlib import Path
from .custome_temp import custome_template_maker



def homeView(request):
    return render(request, 'mainapp/home.html')

def loginView(request):
    jsonData = open('mainapp\private\json\login.json')
    formSchema = json.load(jsonData)
    

    return render(request, 'mainapp/login.html', {'formSchema':custome_template_maker(formSchema)})
