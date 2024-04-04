import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d_temp = dict(i.split('=') for i in lst_in)
d = {}
for i in d_temp:
    d[int(i)] = d_temp[i]
print(*sorted(d.items()))
