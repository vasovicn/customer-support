from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
from django.contrib.admin import SimpleListFilter

# Register your models here.

admin.site.site_header = 'Customer Service Admin'
admin.site.unregister(Group)

#Adding class to filter objects in model Ticket by archive(BooleanField)
class ArchivedTickets(SimpleListFilter):
    title = 'Tickets'
    parameter_name = 'ticket_archive'

    def lookups(self,request, model_admin):
       return (
           ('archived', 'archived'),
       )
    def queryset(self, request, queryset):
        '''lookup archived will show objects where archived field is True
            When nothing is selected in Filter, objects with archived field False will be shown'''
        if not self.value():
            return queryset.exclude(archive=True)
        if self.value() == 'archived':
            return queryset.exclude(archive=False)


class Filter(admin.ModelAdmin):
    list_display = ('subject', 'email', 'date_and_time_for_callback', 'submitted_date_and_time')
    list_filter = (ArchivedTickets,)


#Registering model Ticket and Filtet to be shown in admin panel
admin.site.register(Ticket, Filter)
