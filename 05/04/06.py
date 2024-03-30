numbers = list(map(float, input().split()))
minimum = numbers[0]
for i in numbers:
    if i < minimum:
        minimum = i
print(minimum)
