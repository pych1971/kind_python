number = input()
it = iter(number)
for i in range(len(number)):
    print(next(it), end=' ')
