i = int(input())
d = {}
while i != 0:
    if i in d:
        print(f'значение из кэша: {d[i]}')
    else:
        d[i] = round(i ** (0.5), 2)
        print(d[i])
    i = int(input())
