import sys
import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу
lst_res = list(zip(*[map(int, x.split()) for x in lst_in]))
random.shuffle(lst_res)
lst_res = list(zip(*lst_res))
for i in lst_res:
    print(*i)
