import math

dollar = float(input())
ruble = int(input())
print(f'Вы можете получить {math.trunc(ruble // dollar)}$ за {ruble} рублей по курсу {dollar}')
