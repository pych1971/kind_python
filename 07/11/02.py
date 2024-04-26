def show_menu(func):
    def wrapper(*args, **kwargs):
        for number, word in enumerate(func(*args)):
            print(f'{number + 1}. {word}')

    return wrapper


@show_menu
def get_menu(s):
    return list(s.split())


get_menu('Главная Добавить Удалить Выйти')
