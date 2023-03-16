class BlockErrors:
    def __init__(self, array_errors):
        self.array_errors = array_errors

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if type in self.array_errors or Exception in self.array_errors or BaseException in self.array_errors:
            return True
        return False

if __name__ == '__main__':
    err_types = {Exception}
    with BlockErrors(err_types):
        a = 1 / '0'
    print('Выполнено без ошибок')


