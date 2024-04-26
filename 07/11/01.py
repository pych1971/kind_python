def func_show(func):
    def wrapper(*args, **kwargs):
        print(f'Площадь прямоугольника: {func(*args, **kwargs)}')

    return wrapper


@func_show
def get_sq(width, height):
    return width * height


get_sq(3, 4)
