from django.test import TestCase
from mixer.backend.django import mixer

from .models import Person, Group, Result
from faker import Faker
from testapp.models import TestUser

import tempfile

from faker.providers import date_time

# Create your tests here.
class PersonTestCaseFake(TestCase):
    def setUp(self):
        fake = Faker()
        self.person = mixer.blend(Person)
        self.person.image  = tempfile.NamedTemporaryFile(suffix=".jpg")

        print('=person=')
        print(str(self.person.name), str(self.person.bday), str(self.person.email))
        print((self.person.image))

        user = TestUser.objects.create(username=fake.name(), email=fake.email(), password='1234567890')
        self.person.user = user
        print('=user=')
        print(user.username, '  ', user.email)



    def test_has_image(self):
        self.assertTrue(self.person.has_image())
        print((self.person.image.name))


class ResultTestCaseFake(TestCase):
    def setUp(self):
        self.result = mixer.blend(Result, name='Предмет', subject__name='Физика')
        print('=result=')
        print(self.result.person, '*', self.result.subject, '*', self.result.mark)

    def test_result(self):
        self.assertTrue(self.result.mark > 0)

