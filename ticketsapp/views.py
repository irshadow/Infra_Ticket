from django.shortcuts import render
from mainapp.custome_temp import custome_template_maker
from django.http import HttpResponseRedirect
from django.urls import reverse
import usersapp
import json

import usersapp.views

def ticketIssueView(request):
    if request.user.is_authenticated and request.user.is_active:
        jsonData = open('ticketsapp\private\json\issueTicket.json')
        formSchema = json.load(jsonData)

        return render(request, 'ticketsapp/issue.html', {'formSchema':custome_template_maker(formSchema)})
    else:
        return HttpResponseRedirect(reverse(usersapp.views.loginView))