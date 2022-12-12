from django.test import Client
from django.test import TestCase
from faker import Faker
from mixer.backend.django import mixer
from testapp.models import TestUser

from .models import Person, Group, Result

class OpenViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/group/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 302)

        self.group = mixer.blend(Group, name='Ученики', person__name=('Иванов','Петров'))
        response = self.client.post('/group/', {'name':self.group.name, 'person':self.group.person})
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/group/')
        self.assertTrue('form' in response.context)


    def test_login_req(self):
        client = Client()
        TestUser.objects.create_user(username='tester', email='qw@qwer.com', password='1234567890')

        response = self.client.get('/create/')
        print('вход незалогиненного пользователя ',response.status_code)
        self.assertEqual(response.status_code, 302)

        client.login(username='tester', password='1234567890')
        response = self.client.get('/create/')
        print('вход залогиненного пользователя ',response.status_code)
        self.assertEqual(response.status_code, 200)

