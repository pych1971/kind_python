import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}
for i in lst_in:
    x = i.split()
    if x[1] not in d:
        d[x[1]] = [x[0]]
    else:
        d[x[1]] = d[x[1]] + [x[0]]
print(*sorted(d.items()))
