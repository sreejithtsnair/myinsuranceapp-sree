import json
import unittest
import requests
from project import app

class TestApp(unittest.TestCase):
    token=''
    base_url='http://localhost:5000/api/v1/products'

    def test_1_testToken(self):
        tester = app.test_client(self)
        test_data = {"email":"jd@myinsuranceapp.com","password":"passwordjd"}
        response = tester.post('/api/v1/token',content_type='application/json', json=test_data)        
        data=json.loads(response.text)
        print(f"post token: {data}")
        self.assertEqual(response.status_code, 200)
        if response.status_code==200:
            TestApp.token=data['token']
        
    def test_2_get_restricted(self):
        tester = app.test_client(self)
        print(f"token: {self.token}")
        headers = {"Authorization": f"Bearer {TestApp.token}"}
        response = tester.get('/api/v1/users/', content_type='application/json', headers=headers)
        data=json.loads(response.text)
        print(f"get restricted: {data}")
        self.assertEqual(response.status_code, 200)
