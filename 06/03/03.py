cities = tuple(input().split())
if cities.count('Ульяновск'):
    i = cities.index('Ульяновск')
    cities = cities[:i] + cities[i + 1:]
print(*cities)
