from django.db import models

# Create your models here.

# Лица
class Person(models.Model):
    name = models.CharField(max_length=50)
    bday = models.DateField()
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(upload_to='person', null=True, blank=True)
    # cv = models.FileField()


    def __str__(self):
        return self.name

# предметы
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# учебные группы/классы
class Group(models.Model):
    name = models.CharField(max_length=30)
    person = models.ManyToManyField(Person)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name

# уроки
class Lesson(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# оценки
class Result(models.Model):
    date = models.DateField(auto_now_add=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    mark = models.IntegerField()

    def __str__(self):
        return str(self.date)+' '+self.person.name+' '+str(self.mark)








