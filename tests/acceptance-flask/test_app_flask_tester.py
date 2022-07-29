import json
from tkinter import TRUE
from tokenize import Token
import unittest
import requests

from project.controllers.api.user_controller import api_get_user

class TestApp(unittest.TestCase):
    token=''
    base_url='http://localhost:5000/api/v1'

    def test_5_get_restricted(self):
        tester = Token.test_client(self)
        print(f"token: {self.token}")
        headers = {"Authorization": f"Bearer {TestApp.token}"}
        self.assertTrue(TRUE)
       