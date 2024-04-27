from functools import wraps


def func_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = sum(func(*args))
        return res

    return wrapper


@func_decorator
def get_list(s):
    '''Функция для формирования списка целых значений'''
    return list(map(int, s.split()))


print(get_list("1 2 3 -1 -2 -3"))
