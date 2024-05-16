import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
names = input().split()
print(*random.sample(names, 3))
