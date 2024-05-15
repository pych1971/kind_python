import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
n = [3, 0, 2, 1]
lst = [[int(j) if j in '1234567890' else j for j in i.split(';')] for i in lst_in]
t_sorted = tuple([tuple(sorted(i, key=lambda x: n[i.index(x)])) for i in lst])
