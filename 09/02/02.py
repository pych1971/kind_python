def pb(N):
    sum = 0
    a, b, c = 1, 1, 1
    for i in range(N):
        yield a
        a, b, c = b, c, a + b + c


N = int(input())
print(*list(pb(N)))
