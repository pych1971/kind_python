import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
for i in lst_in:
    while '  ' in i:
        i = i.replace('  ', ' ')
    while ' ' in i:
        i = i.replace(' ', '-')
    print(i)
