def multiply(maximum, minimum):
    return maximum * minimum


numbers = list(map(int, input().split()))
print(multiply(max(numbers), min(numbers)))
