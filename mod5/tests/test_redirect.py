import unittest
from mod5.task4 import Redirect

class TestREdirect(unittest.TestCase):
    def test_stdout(self):
        print('Hello stdout')
        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')

        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        file = open('stdout.txt')
        assert ("Hello stdout.txt" in file.read())

    def test_stderr(self):
        print('Hello stdout')
        stdout_file = open('stdout.txt', 'w')
        stderr_file = open('stderr.txt', 'w')

        with Redirect(stdout=stdout_file, stderr=stderr_file):
            print('Hello stdout.txt')
            raise Exception('Hello stderr.txt')

        file = open('stderr.txt')
        assert ("Exception: Hello stderr.txt" in file.read())