lst1 = [int(i) for i in input().split()]
lst2 = [int(i) for i in input().split()]
lst3 = [lst1[i] + lst2[i] for i in range(len(lst1))]
print(*lst3)
