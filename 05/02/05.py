n = int(input())
ls = []
i = 1
while i <= n:
    if n >= 100:
        print("слишком большое значение n")
        break
    elif i % 3 == 0 and i % 5 == 0:
        ls.append(i)
    i += 1
else:
    print(*ls)
