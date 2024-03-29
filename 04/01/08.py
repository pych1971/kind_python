a, b, c, d = map(int, input().split())
if a - c - 1 > 0 and b - d - 1 > 0 or a - d - 1 > 0 and b - c - 1 > 0:
    print('ДА')
else:
    print('НЕТ')
