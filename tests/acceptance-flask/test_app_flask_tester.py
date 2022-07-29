import json
import unittest
import requests

from project.controllers.api.user_controller import api_get_user

class TestApp(unittest.TestCase):
    token=''
    base_url='http://localhost:5000/api/v1'

    def test_1_get_token(self):
        tester = api_get_user.test_client(self)
        test_data = {"email":"jd@myinsuranceapp.com","password":"passwordjd"}
        response = tester.post('/api/v1/token',content_type='application/json', json=test_data)
        data=json.loads(response.text)
        self.assertEqual(response.status_code, 200)
       