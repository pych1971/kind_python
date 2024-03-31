import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
res = 'ДА'
for i in range(5):
    for j in range(i, 5):
        if lst_in[i][j] != lst_in[j][i]:
            res = 'НЕТ'
            break
    if res == 'НЕТ':
        break
print(res)
