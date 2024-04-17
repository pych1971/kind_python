t_source = tuple(map(int, input().split()))
t_result = tuple()
for i in t_source:
    if i not in t_result:
        t_result += (i,)
print(*t_result)
