def change_do_dish(chars=' !?'):
    def func_decorator(func):
        def wrapper(*args, **kwargs):
            res = ''
            for i in func(*args):
                if i in chars:
                    res += '-'
                else:
                    res += i
            while '--' in res:
                res = res.replace('--', '-')
            return res

        return wrapper

    return func_decorator


@change_do_dish(chars="?!:;,. ")
def convert_to_lat(s):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    res = ''
    for i in s.lower():
        if i in t.keys():
            res += t[i]
        else:
            res += i
    return res


s = input()
print(convert_to_lat(s))
