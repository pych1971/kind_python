def start_decorator(start):
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args) + start
            return res

        return wrapper

    return func_decorator


@start_decorator(start=5)
def convert(s):
    return sum(map(int, s.split()))


s = input()
print(convert(s))
