import json
import unittest
from project import app
from project.persistence.users_dao import *
from flask_jwt_extended import jwt_required, get_jwt_identity


class TestApp(unittest.TestCase):
    token=''

     def test_1_getToken(self):         
        self.assertTrue(True)

    def test_1_get_none(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/products/', content_type='application/json')
        data=json.loads(response.text)
        print(f"get 1: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, [])

    def test_4_testToken(self):
        tester = app.test_client(self)
        test_data = {"email":"user@test.com","password":"passwordjd"}
        response = tester.post('/api/v1/token',content_type='application/json', json=test_data)        
        data=json.loads(response.text)
        print(f"post token: {data}")
        self.assertEqual(response.status_code, 200)
        if response.status_code==200:
            TestApp.token=data['token']
        
    def test_5_get_restricted(self):
        tester = app.test_client(self)
        print(f"token: {self.token}")
        headers = {"Authorization": f"Bearer {TestApp.token}"}

        response = tester.get('/api/v1/restricted', content_type='application/json', headers=headers)
        data=json.loads(response.text)
        print(f"get restricted: {data}")
        self.assertEqual(response.status_code, 200)