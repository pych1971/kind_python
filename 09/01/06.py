cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (cities[x - len(cities) * (x // len(cities))] for x in range(1000000))
for i in range(20):
    print(next(gen), end=' ')
