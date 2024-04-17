t = tuple(map(int, input().split()))
for i in range(len(t)):
    if t.count(t[i]) > 1:
        print(i, end=' ')
