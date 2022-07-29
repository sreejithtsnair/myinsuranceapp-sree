import json
import unittest
import requests

class TestApp(unittest.TestCase):
    token=''
    base_url='http://localhost:5000/api/v1/'

    def test_1_get_Token(self):
        url=f"{self.base_url}/token"
        self.assertTrue(True)
        