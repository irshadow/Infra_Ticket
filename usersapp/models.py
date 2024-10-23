from django.db import models

class Role(models.Model):
    description = models.CharField(null=False, blank=False, max_length=40)

    def __str__(self):
        return '{}'.format(self.description)
    

    
class Department(models.Model):
    name = models.CharField(null=False, blank=False, max_length= 100)

    def __str__(self):
        return '{}'.format(self.name)
    

class User(models.Model):
    fname = models.CharField(null=False, blank=False, max_length=50)
    lname = models.CharField(null=False, blank=False, max_length=50)
    email = models.EmailField(null=False, blank=False, max_length=60, unique=True)
    pword = models.CharField(null=False, blank=False, max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    lastlogin = models.DateTimeField(null=False, blank=False)
    ip = models.IPAddressField(null=False, blank=False)
    isblock = models.BooleanField(null=False, blank=False,default=False)


    def __str__(self):
        return '{}  {} - {}({})'.format(self.fname, self.lname, self.role, self.department)

    

