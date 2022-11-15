from django.core.management.base import BaseCommand
from django.conf import settings
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR,'educenterapp', 'management', 'commands', 'example.txt')
        with open(path, 'r') as f:
            print(f)