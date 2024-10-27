from django.db import models
from servicesapp.models import ServiceModel,DepartmentModel
    
class UserProfileModel(models.Model):
    man = 1
    woman = 2
    gender_choice = ((man, "Man"),
                     (woman, "Woman"))
    gender = models.IntegerField(choices=gender_choice, null=False, blank=False)
    department = models.ForeignKey(DepartmentModel, on_delete=models.PROTECT)
    team = models.ForeignKey(ServiceModel, null= False, blank=False, on_delete=models.PROTECT)
    manager = 1
    head = 2
    expert = 3
    role_choices = ((manager, "Department manager"),
                    (head, "Head of special team"),
                    (expert, "Expert employee"))
    role = models.IntegerField(choices=role_choices, null=False, blank=False)
    ip = models.GenericIPAddressField(null=False, blank=False)
    


    def __str__(self):
        return '{}  {} - {}({})'.format(self.fname, self.lname, self.role, self.department)

    

