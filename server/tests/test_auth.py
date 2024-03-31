import unittest
import json
from flask import url_for
from flask_testing import TestCase
from app import create_app, db
import json
 
class SettingBase(TestCase):
    def create_app(self):
        return create_app("testing")

    def setUp(self):
        db.create_all()
        self.username='admin'
        self.password='admin_password'
 
    def tearDown(self):
        db.session.remove()
        db.drop_all()
 
    def signup(self):
        response = self.client.post(url_for('auth.signup'),
                                    json={
                                        "username": self.username,
                                        "password": self.password,
                                    })

        response_data = json.loads(response.data.decode('utf-8'))
        return response_data, response.status_code
 
class CheckUserAndLogin(SettingBase):
    def test_signup(self):
        data, status_code = self.signup()
        self.assertEqual(data['data']['username'], self.username)
        self.assertEqual(status_code, 200)

    def test_signup_duplicate(self):
        self.signup()
        data, status_code = self.signup()
        self.assertEqual(data['error_code'], 400001)
        self.assertEqual(status_code, 400)
 
if __name__ == '__main__':
    unittest.main()