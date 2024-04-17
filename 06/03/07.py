t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
N = int(input())
l2 = []
for i in range(N):
    l2.append(tuple(t[i][:N]))
t2 = tuple(l2)
for i in t2:
    print(*i)
