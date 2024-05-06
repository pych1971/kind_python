numbers = map(int, input().split())
print(*list(filter(lambda x: 10 <= abs(x) <= 99, numbers)))
