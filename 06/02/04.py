import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
days = {}
for i in lst_in:
    day = i.split()
    if days.get(int(day[0])) == None:
        days[int(day[0])] = day[1]
    else:
        days[int(day[0])] = f'{days[int(day[0])]}, {day[1]}'
for key, value in days.items():
    print(f'{key}: {value}')
