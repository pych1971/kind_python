n = int(input())
res = 'ДА'
for i in range(2, n):
    if n % i == 0:
        res = 'НЕТ'
        break
print(res)
