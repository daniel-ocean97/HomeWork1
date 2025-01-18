from src.decorators import log


def test_log_decorator_error_console(capsys):
    """Функция, которая тестирует декоратор log на функции с ошибкой и выводом в консоль"""

    @log(filename=None)
    def error_func():
        raise ValueError

    error_func()
    message = capsys.readouterr()
    assert message.out == "error_func error: ValueError. Inputs: (), {}\n"


def test_log_decorator_console(capsys):
    """Функция, которая тестирует декоратор log на функции без ошибки и выводом в консоль"""

    @log(filename=None)
    def ok_func(a, b):
        return a + b

    ok_func(1, 2)
    messsage = capsys.readouterr()
    assert messsage.out == "ok_func ok\n"


def test_log_decorator_file():
    """Функция, которая тестирует декоратор log на функции без ошибки и выводом в файл 'test.txt'"""

    @log(filename="test.txt")
    def ok_file_func():
        return True

    ok_file_func()
    with open("test.txt", "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        message = all_lines[-1]
    assert message == "ok_file_func ok\n"


def test_log_error_decorator_file():
    """Функция, которая тестирует декоратор log на функции с ошибкой и выводом в файл 'test.txt'"""

    @log(filename="test.txt")
    def error_file_func():
        raise ValueError

    error_file_func()
    with open("test.txt", "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        message = all_lines[-1]
    assert message == "error_file_func error: ValueError. Inputs: (), {}\n"
