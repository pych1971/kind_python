cities = list(map(lambda x: str(x) if len(x) > 5 else '-', input().split()))
print(*cities)
