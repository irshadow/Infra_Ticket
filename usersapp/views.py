from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponseForbidden
from mainapp.views import homeView
from ticketsapp.views import dispatchView
from django.urls import reverse
import json
from  .models import UserProfileModel

#Load .json schema file from server and passing its data to the login page. I used for statement in te template
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
            upm = UserProfileModel.objects.get(user = request.user)
            if upm.role  == 1 or upm.role == 2 :
                    return HttpResponseRedirect(reverse(dispatchView))
            else: 
                    return HttpResponseRedirect(reverse(homeView))
        else:
            #Read the local login.json file which conaints login form's schema
            rawData = open('usersapp/private/json/login.json')
            rawData = json.load(rawData)
            #Render login form 
            return render(request, 'usersapp/login.html', {'rawData': {'data':rawData, 'message':'Invalid username / password'}}) #We passed json schema to the login.html
    else:
        return HttpResponseRedirect(reverse(index))

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse(homeView)) 

  
