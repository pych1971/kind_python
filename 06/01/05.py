lst = input().split()
d = {}
for i in lst:
    if i[:2] not in d:
        d[i[:2]] = [i]
    else:
        d[i[:2]] = d[i[:2]] + [i]
print(*sorted(d.items()))
