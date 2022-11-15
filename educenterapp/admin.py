from django.contrib import admin

# Register your models here.

from .models import Group, Result, Person, Subject

admin.site.register(Group)
# admin.site.register(Lesson)
admin.site.register(Result)
admin.site.register(Person)
admin.site.register(Subject)