import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
lst_out = [lst_in[i][j] for i in range(len(lst_in) - 1, -1, -1) for j in range(len(lst_in[0]) - 1, -1, -1)]
print(*lst_out)
