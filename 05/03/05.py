numbers = list(map(int, input().split()))
s = 0
for i in numbers:
    if i % 2 != 0:
        s += i
print(s)
