def get_rec_sum(numbers):
    if len(numbers) > 1:
        numbers[0] += numbers.pop()
        get_rec_sum(numbers)
    return numbers[0]


print(get_rec_sum(list(map(int, input().split()))))
