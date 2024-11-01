from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponseForbidden, HttpResponse
from django.urls import reverse
from mainapp.views import homeView
import datetime
import usersapp
import usersapp.models
from .models import TicketModel,DepartmentModel,ServiceModel, CommentModel
import json
from .forms import frmBuilder
import usersapp.views

@login_required
def myTicketsView(request): #Empoyees can see their issued tickets and its status
        context = {
            'tickets': TicketModel.objects.filter(issuer = request.user)
        }
        print(context['tickets'])
        return render(request, "ticketsapp/mytickets.html", context )


@login_required
def closeTicketView(request, tk_id): #experts can close and cancel their tickets
        if request.method == "POST":
            ticket = TicketModel.objects.get(pk=tk_id)
            ticket.closetime= datetime.datetime.now()
            ticket.status = int(request.POST.get('status'))
            comment = request.POST.get('comment')
            upm = get_object_or_404(usersapp.models.UserProfileModel, user = request.user)
            cmt = CommentModel(description= comment, owner = usersapp.models.UserProfileModel.objects.get(id = upm.id), ticket = TicketModel.objects.get(id= tk_id))
            cmt.save()
            ticket.save()
            
            return HttpResponseRedirect(reverse(expertTicketView))
        else:
            return HttpResponse("Request method is not acceptable")

@login_required
def expertTicketView(request):# experts can see their tickets
 
    upm = get_object_or_404(usersapp.models.UserProfileModel, user = request.user)
    context = {
        'tickets': TicketModel.objects.filter(solver = upm.id).exclude(status__in=[3,4])
    }
    return render(request, "ticketsapp/ticket-area.html", context )

@login_required
def editTkView(request, tk_id):
    if request.method == "POST":
        ticket = TicketModel.objects.get(pk=tk_id)
        ticket.solver = usersapp.models.UserProfileModel.objects.get(id = int(request.POST.get('expert')))
        ticket.dispatchtime= datetime.datetime.now()
        ticket.status = 2
        ticket.save()
        
        return HttpResponseRedirect(reverse(dispatchView))
    else:
        return HttpResponse("Request method is not acceptable")

@login_required
def dispatchView(request):
        try:
            upm = get_object_or_404(usersapp.models.UserProfileModel, user = request.user) #fetching UserProfileModel record which is related to the logged in user 
            if (upm) and (upm.role  == 1 or upm.role == 2) : #User can access to the issued ticket if he/she is manager of department or head of a team
                myU = usersapp.models.UserProfileModel.objects.filter(department = upm.department ).exclude(user= request.user)# Manager/head just can see their experts
                context={
                    'pending_tickets': TicketModel.objects.filter(status=1, todepartment = upm.department), #Manager/head just can see their demartment tickets
                    'assigned_tickets': TicketModel.objects.filter(status=2, todepartment = upm.department),
                    'canceled_tickets' :  TicketModel.objects.filter(status__in=[3,4], todepartment = upm.department), #Fetching closed and canceled tickets
                    'users': usersapp.models.UserProfileModel.objects.filter(department = upm.department ).exclude(user= request.user)
                }
                return render(request, "ticketsapp/dispatch.html", context)
        except:
            return HttpResponseForbidden("You don't have permission to access this page")

@login_required
def ticketIssueView(request):
        #Read a local .json schema in order to parsing
        jsonData = open('ticketsapp/private/json/issueTicket.json')
        formSchema = json.load(jsonData) #load json data
        rawForm = frmBuilder(formSchema) #pass the data to form class

        if request.method == "POST": #we need store posted form data if the method is POST
            frm = rawForm(request.POST)
            if frm.is_valid():
                print(frm.cleaned_data["department"])
                ticket_model = TicketModel(issuer = request.user, 
                                           todepartment = DepartmentModel.objects.get(id =  frm.cleaned_data["department"]),
                                           title = ServiceModel.objects.get(id = frm.cleaned_data["title"]),
                                           description = frm.cleaned_data["description"],
                                           priority = frm.cleaned_data["priority"],
                                           status = 1
                                           )
                ticket_model.save()
                return HttpResponseRedirect(reverse(homeView))
        else: #if it's not POST method, then render initial page
            frm = rawForm()
            context = {
                "title": formSchema["title"],
                "form": frm,
                "action":formSchema["action"]
            }

            return render(request, 'ticketsapp/issue.html', context)
