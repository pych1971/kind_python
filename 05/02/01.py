p = [0] * 10
while sum(p) != 5:
    i = int(input())
    if p[i] == 1:
        continue
    else:
        p[i] = 1
print(*p)
