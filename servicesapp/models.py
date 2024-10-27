from django.db import models

class DepartmentModel(models.Model):
    name = models.CharField(null=False, blank=False, max_length= 50)

    def __str__(self):
        return '{}'.format(self.name)

class ServiceModel(models.Model):
    name = models.CharField(null=False, blank=False, max_length=40)
    department = models.ForeignKey(DepartmentModel, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return '{} : ({})'.format(self.name, self.department)

