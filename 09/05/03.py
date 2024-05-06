import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
lst_rec = list(list(map(int, x.split())) for x in lst_in)
res = (zip(*lst_rec))
for i in res:
    print(*i)
