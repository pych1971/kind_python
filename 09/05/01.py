numbers1 = map(int, input().split())
numbers2 = map(int, input().split())
num_zip = zip(numbers1, numbers2)
mul = map(lambda x: x[0] * x[1], list(num_zip))
for i in range(3):
    print(next(mul), end=' ')
