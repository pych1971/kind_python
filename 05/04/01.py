txt = input().lower()
res = -1
for i in range(len(txt) - 1):
    if txt[i:i + 2] == 'ра':
        print(i, end=' ')
        res = ''
print(res)
