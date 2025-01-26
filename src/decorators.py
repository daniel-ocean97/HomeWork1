from functools import wraps


def log(filename=None):
    """Декоратор, который логирует результаты выполнения функции в консоль или файл"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if filename is None:
                try:
                    result = func(*args, **kwargs)
                    print(f"{func.__name__} ok")
                    return result
                except Exception as e:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
            else:
                try:
                    result = func(*args, **kwargs)
                    with open(filename, "a", encoding="utf-8") as f:
                        message = f"{func.__name__} ok\n"
                        f.write(message)
                    return result
                except Exception as e:
                    with open(filename, "a", encoding="utf-8") as f:
                        message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                        f.write(message)

        return wrapper

    return decorator
