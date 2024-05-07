numbers = set(map(int, input().split()))
print(*sorted(numbers, reverse=True)[:4])
