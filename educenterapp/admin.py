from django.contrib import admin

# Register your models here.

from .models import Group, Result, Person, Subject


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'group_persons']

admin.site.register(Group, GroupAdmin)
admin.site.register(Result)
admin.site.register(Person)
admin.site.register(Subject)
