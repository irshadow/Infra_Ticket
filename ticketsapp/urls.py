from django.urls import path
from .views import ticketIssueView, dispatchView, editTkView,expertTicketView, closeTicketView, myTicketsView

urlpatterns = [
    path('ticket/', ticketIssueView, name="ticket"),
    path('dispatch/', dispatchView, name="dispatch"),
    path('dispatch/<int:tk_id>',editTkView, name="editTicket" ),
    path('expertTickets/', expertTicketView, name="exTickets" ),
    path('expertTickets/<int:tk_id>', closeTicketView, name="changeStatus" ),
    path('mytickets/', myTicketsView, name= "myTickets")
]

