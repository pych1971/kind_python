import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
s = set()
for i in lst_in:
    s.add(i.split(':')[0])
print(len(s))
