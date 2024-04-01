lst = [float(number) for i, number in enumerate(input().split()) if i % 2 == 0]
print(*lst)
