from src.decorators import log


def test_log_decorator_error(capsys):
    @log(filename=None)
    def error_func():
        raise ValueError
    error_func()
    message = capsys.readouterr()
    assert message.out == 'error_func error: ValueError. Inputs: (), {}\n'


def test_log_decorator(capsys):
    @log(filename=None)
    def ok_func(a, b):
        return a + b
    ok_func(1, 2)
    messsage = capsys.readouterr()
    assert messsage.out == "ok_func ok\n"