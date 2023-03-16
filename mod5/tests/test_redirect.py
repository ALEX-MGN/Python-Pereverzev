import unittest
from mod5.task4 import Redirect

class TestREdirect(unittest.TestCase):
    def test_stdout(self):
        try:
            print('Hello stdout')
            stdout_file = open('stdout.txt', 'w')
            stderr_file = open('stderr.txt', 'w')

            with Redirect(stdout=stdout_file, stderr=stderr_file):
                print('Hello stdout.txt')
                raise Exception('Hello stderr.txt')

            print('Hello stdout again')
            raise Exception('Hello stderr')
        except:
            return False
        assert ("Hello stdout.txt" == stdout_file.read())

    def test_stderr(self):
        try:
            print('Hello stdout')
            stdout_file = open('stdout.txt', 'w')
            stderr_file = open('stderr.txt', 'w')

            with Redirect(stdout=stdout_file, stderr=stderr_file):
                print('Hello stdout.txt')
                raise Exception('Hello stderr.txt')

            print('Hello stdout again')
            raise Exception('Hello stderr')
        except:
            return False
        assert ("Traceback (most recent call last):File '/home/user/Desktop/Python-Pereverzev/mod5/task4.py', line 31, in <module> raise Exception('Hello stderr.txt') Exception: Hello stderr.txt" == stderr_file.read())