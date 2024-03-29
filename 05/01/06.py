number = list(map(int, input()))
multi = 1
i = 0
while i < len(number):
    multi *= number[i]
    i += 1
print(multi)
