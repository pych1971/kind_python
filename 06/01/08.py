import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}
for i in lst_in:
    if i in d:
        print(f'Взято из кэша: {d[i]}')
    else:
        d[i] = f'HTML-страница для адреса {i}'
        print(d[i])
