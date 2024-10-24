from django.urls import path
from .views import ticketIssueView

urlpatterns = [
    path('ticket/', ticketIssueView)
]

