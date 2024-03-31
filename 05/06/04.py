import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
res = 'ДА'
for i in range(4):
    for j in range(4):
        if lst_in[i][j] + lst_in[i + 1][j] + lst_in[i][j + 1] + lst_in[i + 1][j + 1] > 1:
            res = 'НЕТ'
    if res == 'НЕТ':
        break
print(res)
