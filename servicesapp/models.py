from django.db import models

class Service(models.Model):
    name = models.CharField(null=False, blank=False, max_length=40)

    def __str__(self):
        return '{}'.format(self.name)

