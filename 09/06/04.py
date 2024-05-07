lst1 = sorted(list(map(int, input().split())))
lst2 = sorted(list(map(int, input().split())), reverse=True)
res = list(zip(lst1, lst2))
print(*[i[0] + i[1] for i in res])
