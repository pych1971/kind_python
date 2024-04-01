N = int(input())
lst = [[i] * N for i in range(N)]
for i in range(N):
    print(*lst[i])
