from django.contrib import admin

# Register your models here.

from .models import Group, Result, Person, Subject


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'group_persons']


def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'bday', 'email', 'is_active']
    actions = [set_active]



admin.site.register(Group, GroupAdmin)
admin.site.register(Result)
admin.site.register(Person, PersonAdmin)
admin.site.register(Subject)
