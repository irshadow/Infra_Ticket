from django.db import models
from usersapp.models import UserProfileModel
from servicesapp.models import ServiceModel,DepartmentModel
    
class TicketModel(models.Model):
    issuer = models.CharField(null=False, blank=False, max_length=60)
    todepartment = models.ForeignKey(DepartmentModel, on_delete=models.PROTECT)
    title = models.ForeignKey(ServiceModel, on_delete=models.PROTECT)
    description = models.TextField(null=False, blank=False, max_length=200)
    
    immediately = 1
    high = 2
    medium = 3
    low = 4
    priority_choices = ((immediately, "Immediately"),
                        (high, "High"),
                        (medium, "Medium"),
                        (low, "Low"))
    priority = models.IntegerField(choices=priority_choices, null=False, blank=False)
    solver = models.ForeignKey(UserProfileModel,null=True, blank=True, on_delete=models.PROTECT)
    
    pending = 1
    assigned = 2
    canceled = 3
    finished = 4
    status_choices = ((pending, "Pending"),
                      ((assigned, "Assigned")),
                      (canceled, "Canceled"),
                      (finished, "Finished"))
    status =models.IntegerField(choices= status_choices,null=True,blank=True)
    issuetime = models.DateTimeField(auto_now_add=True)
    dispatchtime = models.DateTimeField(null=True, blank=True)
    closetime = models.DateTimeField(null=True, blank=False)

    def __str__(self):
        return '{} - {} - ({})'.format(self.issuer, self.title, self.description, self.priority, self.issuetime, self.solver, self.status, self.dispatchtime, self.closetime)
    
class CommentModel(models.Model):
    description = models.TextField(blank=True,max_length=200)
    dateofcomment = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(UserProfileModel, on_delete=models.PROTECT)
    ticket = models.ForeignKey(TicketModel, on_delete=models.CASCADE)

    def __str__(self):
        return '({}) {} - Date: {}'.format(self.owner, self.description, self.dateofcomment)