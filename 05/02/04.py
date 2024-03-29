names = list(input().split())
res = 'НЕТ'
i = 0
while i < len(names):
    if names[i][0].upper() == names[i][-1].upper():
        res = 'ДА'
        break
    i += 1
print(res)
