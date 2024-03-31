numbers = list(map(int, input().split()))
for i in range(len(numbers) - 1):
    minimum = numbers[i]
    id = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < minimum:
            minimum = numbers[j]
            id = j
    if id != i:
        numbers[i], numbers[id] = numbers[id], numbers[i]
print(*numbers)
