from django.core.management.base import BaseCommand
from educenterapp.models import Person, Group, Subject, Lesson, Result
import datetime, random

class Command(BaseCommand):

    def handle(self, *args, **options):
        # очищаем данные из базы
        Subject.objects.all().delete()
        Group.objects.all().delete()
        Person.objects.all().delete()
        Lesson.objects.all().delete()
        Result.objects.all().delete()


        # проверочная печать
        print('БД очищена')
