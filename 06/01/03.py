d = dict([i.split('=') for i in input().split()])
s = 0
for i in ['house', 'True', '5']:
    if i in d:
        s += 1
print('ДА') if s == 3 else print('НЕТ')
