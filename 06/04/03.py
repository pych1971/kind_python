txt = input()
s = set()
for i in txt:
    if i.isnumeric():
        s.add(i)
if s:
    print(*sorted(s))
else:
    print('НЕТ')
