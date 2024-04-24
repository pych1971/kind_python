numbers = map(float, input().split())
cities = input().split()
lst = (*numbers, *cities)
print(*lst)
