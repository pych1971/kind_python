cities = list(input().split())
res = 'ДА'
i = 0
while i < len(cities):
    if len(cities[i]) < 6:
        res = 'НЕТ'
        break
    i += 1
print(res)
