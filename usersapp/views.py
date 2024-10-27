from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from mainapp.views import homeView
from django.urls import reverse
import json

def index(request):
    #Read the local login.json file which conaints login form's schema
    rawData = open('usersapp/private/json/login.json')
    rawData = json.load(rawData)
    #Render login form 
    return render(request, 'usersapp/login.html', {'rawData': rawData}) #We passed json schema to the login.html

def doLogin(request):
    #Request will process if user sent login data to this view by POST method 
    if request.method == 'POST':
        username = request.POST.get('username')
        pword = request.POST.get('password')
        user = authenticate(request, username= username, password= pword)
        if user is not None: #If user exists in the database do login
            login(request, user)
            return HttpResponseRedirect(reverse(homeView))
        else:
            #Read the local login.json file which conaints login form's schema
            rawData = open('usersapp/private/json/login.json')
            rawData = json.load(rawData)
            #Render login form 
            return render(request, 'usersapp/login.html', {'rawData': {'data':rawData, 'message':'Invalid username / password'}}) #We passed json schema to the login.html
    else:
        return render(reverse(index))

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(homeView)) 

  
