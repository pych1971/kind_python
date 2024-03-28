lst = list(map(int, input().split()))
last = lst.pop()
lst.append(last % 2 != 0)
print(*lst)
