import unittest
from mod3.task1and3.flaskwork import app
from freezegun import freeze_time
import datetime
class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_max_number_in_series_of_two(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    @freeze_time('2023-03-04')
    def test_can_get_correct_username_with_weekdate(self):
        weekdate = "Хорошей субботы!"
        response = self.app.get(self.base_url + 'Хорошей среды!')
        response_text = response.data.decode().split(".")[1]
        self.assertTrue(weekdate in response_text)
