n = int(input())
cur = [64, 32, 16, 8, 4, 2, 1]
for i in cur:
    while n >= i:
        print(i, end=' ')
        n -= i
