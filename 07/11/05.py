def remove_dashes(func):
    def wrapper(s):
        res = func(s)
        while '--' in res:
            res = res.replace('--', '-')
        return res

    return wrapper


@remove_dashes
def convert_to_lat(s):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    res = ''
    for i in s:
        if i.lower() in t:
            res += t[i.lower()]
        elif i in ": ;.,_":
            res += '-'
        else:
            res += i.lower()
    return res


s = input()
print(convert_to_lat(s))
