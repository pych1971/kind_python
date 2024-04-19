def len_str(txt):
    return txt, len(txt)


cities = input().split()
d = {len_str(city)[0]: len_str(city)[1] for city in cities}

a = sorted(d, key=lambda x: d[x])
print(*a)
