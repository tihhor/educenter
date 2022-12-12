from django.contrib import admin
from django.db.models import F

# Register your models here.

from .models import Group, Result, Person, Subject

class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'group_persons']

def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

def add_mark(modeladmin, request, queryset):
    queryset.update(mark=F('mark')+1)

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'bday', 'email', 'is_active']
    actions = [set_active]

class ResultAdmin(admin.ModelAdmin):
    list_display = ['person','subject', 'mark', 'user']
    actions = [add_mark]



admin.site.register(Group, GroupAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Subject)
