import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
dict_in = {}
for i in lst_in:
    dict_in[i.split('=')[0]] = int(i.split('=')[1])
lst_sort = sorted(dict_in.keys(), key=lambda x: dict_in[x], reverse=True)
print(*lst_sort)
