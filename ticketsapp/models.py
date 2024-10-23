from django.db import models
from usersapp.models import User,Department
from servicesapp.models import Service

class Priority(models.Model):
    descripiton = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return '{}'.format(self.descripiton)
    
class Status(models.Model):
    description = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return '{}'.format(self.description)
    
class Ticket(models.Model):
    issuer = models.CharField(null=False, blank=False, max_length=60)
    title = models.ForeignKey(Service, on_delete=models.PROTECT)
    description = models.TextField(null=False, blank=False, max_length=200)
    todepartment = models.ForeignKey(Department, on_delete=models.PROTECT)
    solver = models.ForeignKey(User, on_delete=models.PROTECT)
    status =models.ForeignKey(Status, on_delete=models.PROTECT)
    issuetime = models.DateTimeField(auto_now_add=True)
    dispatchtime = models.DateTimeField(blank=True)
    closetime = models.DateTimeField(null=True, blank=False)


    def __str__(self):
        return '{} - {} - ({})'.format(self.issuer, self.service, self.status)
    
class Comment(models.Model):
    description = models.TextField(blank=True,max_length=200)
    dateofcomment = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - Date: {}'.format(self.owner, self.dateofcomment)