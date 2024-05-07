cities = input().split()
for i in list(zip(*[iter(cities)] * 3)):
    print(*i)
