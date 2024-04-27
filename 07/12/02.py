def add_tag(tag='h1'):
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            res = f'<{tag}>{func(*args)}</{tag}>'
            return res

        return wrapper

    return func_decorator


@add_tag(tag='div')
def make_lower(s):
    return s.lower()


s = input()
print(make_lower(s))
