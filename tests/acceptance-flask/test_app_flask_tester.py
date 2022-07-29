import json
import unittest
from project import app 

class TestApp(unittest.TestCase):

    token=''
       
    def test_1_get_valid_token(self):
        tester = app.test_client(self)
        print(f"token: {self.token}")
        headers = {"Authorization": f"Bearer {TestApp.token}"}
        response = tester.get('/api/v1/users/1/products', content_type='application/json', headers=headers)
        data=json.loads(response.text)
        print(f"get_user_products: {data}")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data)>0)

    def test_2_get_user_products_invalid_token(self):
        tester = app.test_client(self)
        invalid_fake_token='DJ8OW5OI0CPGJBgSNlGwO0x4YF7qbYKVv7KOO-N0eFtDUzXOrL7F9Xd'
        headers = {"Authorization": f"Bearer {invalid_fake_token}"}
        response = tester.get('/api/v1/users/1/products', content_type='application/json', headers=headers)
        data=json.loads(response.text)
        print(f"get_user_products: {data}")
        self.assertTrue(response.status_code > 400)

    def test_3_get_Token(self):         
        tester = app.test_client(self)
        user_data = {"email":"jd@myinsuranceapp.com","password":"passwordjd"}
        response = tester.post('/api/v1/token', content_type='application/json', json = user_data)
        data=json.loads(response.text)
        print(f"post token: {data}")
        self.assertEqual(response.status_code, 200)
        if response.status_code==200:
            TestApp.token=data['token']
      
