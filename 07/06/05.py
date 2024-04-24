import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# здесь продолжайте программу (используйте список lst_in и menu)
menu2 = dict()
for i in lst_in:
    menu2[i.split('=')[0]] = i.split('=')[1]
menu = {**menu, **menu2}
