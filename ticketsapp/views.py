from django.shortcuts import render
from mainapp.custome_temp import custome_template_maker
import json

def ticket(request):
    jsonData = open('mainapp\private\json\issueTicket.json')
    formSchema = json.load(jsonData)

    return render(request, 'ticketsapp/issue.html', {'formSchema':custome_template_maker(formSchema)})
