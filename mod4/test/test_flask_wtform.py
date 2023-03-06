import unittest
from mod4.flask_wtform import app

class TestFlaskWtform(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = 'https://localhost/'

    def test_all_correct(self):
        response = self.app.post(self.base_url + 'registration',
                                 data={"email": "test@example.com", "phone": 9999999999, "name": "Aleksandr", "address": "Prostokvashino", "index": 666})
        assert (response.status_code == 200)

    def test_all_with_comment_correct(self):
        response = self.app.post(self.base_url + 'registration',
                                 data={"email": "test@example.com", "phone": 9999999999, "name": "Aleksandr", "address": "Prostokvashino", "index": 666, "comment": "the max faster,please"})
        assert (response.status_code == 200)

    def test_email_fail_notdog(self):
        response = self.app.post(self.base_url + 'registration',
                                 data={"email": "testexample.com", "phone": 9999999999, "name": "Aleksandr", "address": "Prostokvashino", "index": 666})
        assert (response.status_code == 400)

    def test_email_fail(self):
        response = self.app.post(self.base_url + 'registration',
                                 data={"email": 66666, "phone": 9999999999, "name": "Aleksandr", "address": "Prostokvashino", "index": 666})
        assert (response.status_code == 400)

    def test_without_email_fail(self):
        response = self.app.post(self.base_url + 'registration',
                                 data={"phone": 9999999999, "name": "Aleksandr", "address": "Prostokvashino", "index": 666})
        assert (response.status_code == 400)

    def test_short_phone_fail(self):
        response = self.app.post(self.base_url + 'registration',
                                 data={"email": "test@example.com", "phone": 999, "name": "Aleksandr", "address": "Prostokvashino", "index": 666})
        assert (response.status_code == 400)

    def test_phone_fail(self):
        response = self.app.post(self.base_url + 'registration',
                                 data={"email": "test@example.com", "phone": "999", "name": "Aleksandr", "address": "Prostokvashino", "index": 666})
        assert (response.status_code == 400)

    def test_without_phone_fail(self):
        response = self.app.post(self.base_url + 'registration',
                                 data={"email": "test@example.com", "name": "Aleksandr", "address": "Prostokvashino", "index": 666})
        assert (response.status_code == 400)

    def test_without_name_fail(self):
        response = self.app.post(self.base_url + 'registration',
                                 data={"email": "test@example.com", "phone": 9999999999, "address": "Prostokvashino", "index": 666})
        assert (response.status_code == 400)

    def test_without_address_fail(self):
        response = self.app.post(self.base_url + 'registration',
                                 data={"email": "test@example.com", "phone": 9999999999, "name": "Aleksandr", "index": 666})
        assert (response.status_code == 400)

    def test_index_fail(self):
        response = self.app.post(self.base_url + 'registration',
                                 data={"email": "test@example.com", "phone": 9999999999, "name": "Aleksandr", "address": "Prostokvashino", "index": "none"})
        assert (response.status_code == 400)

    def test_without_index_fail(self):
        response = self.app.post(self.base_url + 'registration',
                                 data={"email": "test@example.com", "phone": 9999999999, "name": "Aleksandr", "address": "Prostokvashino"})
        assert (response.status_code == 400)