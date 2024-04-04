d = dict([i.split('=') for i in input().split()])
for i in d:
    d[i] = int(d[i])
print(*sorted(d.items()))
