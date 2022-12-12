import requests
import pprint

response = requests.get('http://127.0.0.1:8000/api/v0/person/', auth=('tihhor', 'tihhor'))
pprint.pprint(response.json())
print('==================')

response = requests.get('http://127.0.0.1:8000/api/v0/person/', auth=('student', 'mozg1234'))
pprint.pprint(response.json())

token = 'd2ba6eab4ce9d8ba63d67d5df24f23be5b2addb2'
headers = {'Authorization': f'Token {token}'}
print('xxxxxxxxxxxxxxxxxxxx')
response = requests.get('http://127.0.0.1:8000/api/v0/person/', headers=headers)
pprint.pprint(response.json())

