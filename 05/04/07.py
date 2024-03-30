numbers = list(map(float, input().split()))
for i, n in enumerate(numbers):
    if n < 0:
        numbers[i] = -1.0
print(*numbers)
