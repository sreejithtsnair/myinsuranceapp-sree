import json
import unittest
from project.controllers.api.user_controller import api_get_user_products, api_get_users, api_update_user


class TestApp(unittest.TestCase):
    token=''

    def test_1_get_none(self):
        tester = api_get_users.test_client(self)
        response = tester.get('/api/v1/users/2/products/', content_type='application/json')
        data=json.loads(response.text)
        print(f"get 2: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, [])

    def test_2_post(self):
        tester = api_update_user.test_client(self)
        test_data = {"country": "India",
                     "email": "sree@s.com",
                     "fullname": "sree"}
        response = tester.post('/api/v1/users/1',content_type='application/json', json=test_data)
        data=json.loads(response.text)
        print(f"post: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['1'] != None)


    def test_3_get_none(self):
        tester = api_get_user_products.test_client(self)
        response = tester.get('/api/v1/users/2/products', 
        content_type='application/json')
        data=json.loads(response.text)
        print(f"get 2: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data)>0)