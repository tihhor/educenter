from django.db import models
from django.utils.functional import cached_property

# from django.contrib.auth.models import User
from testapp.models import TestUser

class TimeStamp(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class ActiveManager(models.Manager):
    def get_queryset(self):
        all_objects = super.get_queryset()
        return all_objects.filter(is_active=True)

# Лица
class Person(TimeStamp):

    objects = models.Manager()
    active_objects = ActiveManager()

    name = models.CharField(max_length=50)
    bday = models.DateField()
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(upload_to='person', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def has_image(self):
        return (self.photo is not None)

    @cached_property
    def get_all_subj(self):
        subjects = Subject.objects.all()
        return subjects


# предметы
class Subject(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

# учебные группы
class Group(models.Model):
    name = models.CharField(max_length=30)
    person = models.ManyToManyField(Person)
    def __str__(self):
        return self.name
    def group_persons(self):
        persons = self.person.all()
        result = ';  '.join([item.name for item in persons])
        return result

# оценки
class Result(TimeStamp):
    date = models.DateField(auto_now_add=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.IntegerField()
    user = models.ForeignKey(TestUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)+' '+self.person.name+' '+str(self.mark)






