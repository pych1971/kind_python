txt = input().split()
s = set()
for i in txt:
    s.add(i.lower())
print(len(s))
