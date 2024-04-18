def measure(numbers):
    print(f'Min = {min(numbers)}, max = {max(numbers)}, sum = {sum(numbers)}')


measure(list(map(int, input().split())))
