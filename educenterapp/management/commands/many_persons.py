from django.core.management import BaseCommand
from mixer.backend.django import mixer

from educenterapp.models import Person, Group, Result, Subject, TestUser

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Person.objects.all().delete()
        for i in range(300):
            print(i)
            mixer.blend(Person)
            mixer.blend(Result)