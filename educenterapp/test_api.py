from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

# factory = APIRequestFactory()
# request = factory.post('/api/v0/', {'title': 'new idea'}, format='json')

client = APIClient()
client.login(username='tihhor', password='tihhor')

response = client.get('http://127.0.0.1:8000/api/v0/person/')
assert response.status_code == 200