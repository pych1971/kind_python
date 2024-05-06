cities = filter(lambda x: len(x) > 5, list(input().split()))
for i in range(3):
    print(next(cities), end=' ')
