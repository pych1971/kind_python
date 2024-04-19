def len_str(txt):
    return len(txt) >= 6


cities = input().split()
lst = []
for city in cities:
    if len_str(city):
        lst.append(city)

print(*lst)
