N = int(input())
lst = []
for i in range(N):
    lst.append([1] * N)
for i in range(len(lst)):
    lst[i][-1] = 5
    print(*lst[i])
