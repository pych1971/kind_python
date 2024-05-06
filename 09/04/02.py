import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
items = tuple(map(tuple, (x.split('=') for x in lst_in)))
items_filter = list(filter(lambda x: int(x[1]) >= 500, items))
for i in items_filter:
    print(i[0], end=' ')
