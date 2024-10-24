from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
import ticketsapp
from django.urls import reverse
import json
from mainapp.custome_temp import custome_template_maker
import ticketsapp.views

def index(request):



    rawData = open('usersapp/private/json/login.json')
    rawData = json.load(rawData)

    return render(request, 'usersapp/login.html', {'rawData': rawData})









    # if request.user.is_authenticated and request.user.is_active:
    #     return HttpResponseRedirect(reverse(ticketsapp.views.ticketIssueView))
    # else:
    #     jsonData = open('usersapp\private\json\login.json')
    #     formSchema = json.load(jsonData)
    #     return render(request, 'usersapp/login.html', {'formSchema':custome_template_maker(formSchema)})


def doLogin(request):












    if request.method == 'POST':
        emailAddress = request.POST.get('emailaddress')
        password = request.POST.get('password')

        user = authenticate(request, email= emailAddress, pword= password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reversed(request,ticketsapp.views.ticketView))
        else:
            # jsonData = open('usersapp\private\json\login.json')
            # formSchema = json.load(jsonData)

            # formSchema = custome_template_maker(formSchema)
            # formSchema.update({'loginFailed': 'invalid username or password'})
            # print(formSchema)
            # return render(request, 'usersapp/login.html', {'formSchema': formSchema})
            return HttpResponseRedirect(reverse(index))
        
    else:
        # jsonData = open('usersapp\private\json\login.json')
        # formSchema = json.load(jsonData)
        # return render(request, 'usersapp/login.html', {'formSchema':custome_template_maker(formSchema)})
        return HttpResponseRedirect(reverse(index))
  
