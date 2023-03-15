import unittest
from mod5.task2 import app

class TestFlaskWtform(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.base_url = 'https://localhost/'

    def test_timeout(self):
        response = self.app.post(self.base_url + 'run_code',
                                 data={"code": "import time; time.sleep(2)", "timeout": 1})
        assert (response.text.split(": ")[-1] == "True")

    def test_timeout_long(self):
        response = self.app.post(self.base_url + 'run_code',
                                 data={"code": "import time; time.sleep(2)", "timeout": 31})
        assert (response.status_code == 400)

    def test_wrong_data_in_timeout(self):
        response = self.app.post(self.base_url + 'run_code',
                                 data={"code": "import time; time.sleep(2)", "timeout": "aaaaaa"})
        assert (response.status_code == 400)

    def test_wrong_data(self):
        response = self.app.post(self.base_url + 'run_code',
                                 data={"code": 'print(123)"; echo "hacked', "timeout": 12})
        assert ("hacked" not in response.text)