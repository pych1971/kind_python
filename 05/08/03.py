N = int(input())
lst = [[0] * i + [1] + [0] * (N - i - 1) for i in range(N)]
for i in range(N):
    print(*lst[i])
