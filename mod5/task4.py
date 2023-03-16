import sys
from traceback import format_exc

class Redirect:
    def __init__(self, stdout = "", stderr = ""):
        self.stdout = stdout
        self.stderr = stderr
        self.standart = sys.stdout

    def __enter__(self):
        if(self.stdout != ""):
            sys.stdout = self.stdout
        return self

    def __exit__(self, type, value, traceback):
        if (self.stderr != ""):
            self.stderr.write(format_exc())
            self.stderr.close()
        if (self.stdout != ""):
            self.stdout.close()
        sys.stdout = self.standart
        return True

if __name__ == '__main__':
    print('Hello stdout')
    stdout_file = open('stdout.txt', 'w')
    stderr_file = open('stderr.txt', 'w')

    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print('Hello stdout.txt')
        raise Exception('Hello stderr.txt')

    print('Hello stdout again')
    raise Exception('Hello stderr')