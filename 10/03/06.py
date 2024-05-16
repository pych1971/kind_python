import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = int(input())
P = [[0] * N for i in range(N)]

# здесь продолжайте программу
for n in range(10):
    while True:
        x = random.randint(0, N - 1)
        y = random.randint(0, N - 1)
        s = 0
        if P[x][y] != 1:
            for i in range(x - 1, x + 2):
                if i < 0 or i > N - 1:
                    continue
                if s > 0:
                    break
                for j in range(y - 1, y + 2):
                    if j < 0 or j > N - 1:
                        continue
                    else:
                        s += P[i][j]
                        if s > 0:
                            break
            if s == 0:
                P[x][y] = 1
                break
for i in P:
    print(*i)
