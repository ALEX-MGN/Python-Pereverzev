import unittest
from mod3.task1and3 import flaskwork

class TestFinance(unittest.TestCase):
    def setUp(self):
        flaskwork.app.config['TESTING'] = True
        flaskwork.app.config['DEBUG'] = False
        self.app = flaskwork.app.test_client()
        flaskwork.storage = {2022: {12: 300, 11: 200, 10: 100}}

    def test_add(self):
        response = self.app.get('add/20221211/100')
        response_text = response.data.decode()
        self.assertTrue("Трата добавлена" in response_text)

    def test_add_two_time(self):
        self.app.get('add/20221211/100')
        self.app.get('add/20221211/1')
        response = self.app.get('calculate/2022/12')
        response_text = response.data.decode()
        self.assertTrue("401" in response_text)

    def test_add_fake_data(self):
        response = self.app.get('add/2022aa11/100')
        response_text = response.data.decode()
        self.assertTrue("Неверные значения" in response_text)

    def test_calculate_year(self):
        response = self.app.get('calculate/2022')
        response_text = response.data.decode()
        self.assertTrue("600" in response_text)

    def test_calculate_year_add(self):
        self.app.get('add/20221211/600')
        response = self.app.get('calculate/2022')
        response_text = response.data.decode()
        self.assertTrue("1200" in response_text)

    def test_calculate_year_month(self):
        response = self.app.get('calculate/2022/12')
        response_text = response.data.decode()
        self.assertTrue("300" in response_text)

    def test_calculate_year_month_add(self):
        self.app.get('add/20221211/50')
        response = self.app.get('calculate/2022/12')
        response_text = response.data.decode()
        self.assertTrue("350" in response_text)

    def test_calculate_year_error(self):
        response = self.app.get('calculate/2020')
        response_text = response.data.decode()
        self.assertTrue("Значение о 2020 годе отсутствуют" in response_text)

    def test_calculate_year_month_error(self):
        response = self.app.get('calculate/2022/05')
        response_text = response.data.decode()
        self.assertTrue("Значение о 2022 годе 5 месяце отсутствуют" in response_text)