sum = 1000
n = int(input())
i = 1
while i <= n:
    sum *= 1.05
    i += 1
print(round(sum, 2))
