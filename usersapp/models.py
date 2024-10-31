from django.db import models
from servicesapp.models import ServiceModel,DepartmentModel
from django.contrib.auth.models import User

class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    man = 1
    woman = 2
    gender_choices = ((man, "Man"),
                     (woman, "Woman"))
    gender = models.IntegerField(choices=gender_choices, null=False, blank=False)
    department = models.ForeignKey(DepartmentModel, on_delete=models.PROTECT)
    team = models.ForeignKey(ServiceModel,blank=True, on_delete=models.PROTECT)
    manager = 1
    head = 2
    expert = 3
    role_choices = ((manager, "Department manager"),
                    (head, "Head of special team"),
                    (expert, "Expert employee"))
    role = models.IntegerField(choices=role_choices, null=False, blank=False)
    ip = models.GenericIPAddressField(null=True, blank=True, editable=False)
    


    def __str__(self):
        return '{}'.format(self.user.get_full_name())

    

