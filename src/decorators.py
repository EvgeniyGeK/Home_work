from functools import wraps


def log(filename=None):
    """Декоратор автоматически записывает детали выполнения функции."""
    def decor_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func_result = func(*args, **kwargs)
                log_func_info = f'{func.__name__} ok'
                if filename:
                    with open(filename, 'a', encoding='utf-8') as text:
                        text.write(log_func_info)
                        text.write('\n')
                else:
                    print(log_func_info)
                return func_result
            except Exception as e:
                info_error = f'{func.__name__} Ошибка: {type(e).__name__}. Inputs: {args}, {kwargs}'
                if filename:
                    with open(filename, 'a', encoding='utf-8') as text:
                        text.write(info_error)
                        text.write('\n')
                else:
                    print(info_error)
                raise e
        return wrapper
    return decor_func


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y

my_function(10, 0)
