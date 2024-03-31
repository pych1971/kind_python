st = input()
it = iter(st)
i = next(it)
while i != ' ':
    print(i, end='')
    i = next(it)
