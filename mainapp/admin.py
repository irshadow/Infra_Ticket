from django.contrib import admin
from usersapp.models import UserProfileModel
from ticketsapp.models import TicketModel, CommentModel
from servicesapp.models import DepartmentModel, ServiceModel

class userProfileAdmin (admin.ModelAdmin):
    list_display = ['user', 'role', 'department', 'team' ]

class commentAdmin(admin.ModelAdmin):
    list_display = ['description']


class departmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    

class ticketAdmin(admin.ModelAdmin):
    list_display = ['issuer','title' ,  'description', 'priority', 'status']

class serviceAdmin(admin.ModelAdmin):
    list_display=['name', 'department']

admin.site.register(UserProfileModel,userProfileAdmin)
admin.site.register(DepartmentModel,departmentAdmin)
admin.site.register(ServiceModel, serviceAdmin)
admin.site.register(TicketModel, ticketAdmin)
admin.site.register(CommentModel, commentAdmin)

