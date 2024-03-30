cities = list(input().split())
res = 'ДА'
for i in range(1, len(cities)):
    if (cities[i - 1][-1].lower() not in 'ьъы' and cities[i - 1][-1].lower() != cities[i][0].lower()) or (
            cities[i - 1][-1].lower() in 'ьъы' and cities[i - 1][-2].lower() != cities[i][0].lower()):
        res = 'НЕТ'
        break
print(res)
