import unittest
from mod5.task3 import BlockErrors

class TestBLockErrors(unittest.TestCase):
    def test_ignore_error(self):
        try:
            err_types = {ZeroDivisionError, TypeError}
            with BlockErrors(err_types):
                a = 1 / 0
            print('Выполнено без ошибок')
            assert True
        except:
            assert False

    def test_error_tipping_over_higher(self):
        try:
            err_types = {ZeroDivisionError}
            with BlockErrors(err_types):
                a = 1 / '0'
            print('Выполнено без ошибок')
            assert False
        except:
            assert True

    def test_error_tipping_over_higher_inside(self):
        try:
            outer_err_types = {TypeError}
            with BlockErrors(outer_err_types):
                inner_err_types = {ZeroDivisionError}
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
                print('Внутренний блок: выполнено без ошибок')
            print('Внешний блок: выполнено без ошибок')
            assert True
        except:
            assert False

    def test_ignore_error_subsidiaries(self):
        try:
            err_types = {Exception}
            with BlockErrors(err_types):
                a = 1 / '0'
            print('Выполнено без ошибок')
            assert True
        except:
            assert False