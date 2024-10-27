from django.contrib import admin
from usersapp.models import UserProfileModel
from ticketsapp.models import TicketModel
from servicesapp.models import DepartmentModel, ServiceModel

class userAdmin (admin.ModelAdmin):
    list_display = ['role', 'department', 'team']
class departmentAdmin(admin.ModelAdmin):
    list_display = ['name']

class ticketAdmin(admin.ModelAdmin):
    list_display = ['issuer', 'description', 'solver', 'priority', 'status']

class serviceAdmin(admin.ModelAdmin):
    list_display=['name', 'department']

admin.site.register(UserProfileModel,userAdmin)
admin.site.register(DepartmentModel,departmentAdmin)
admin.site.register(ServiceModel, serviceAdmin)
admin.site.register(TicketModel, ticketAdmin)


