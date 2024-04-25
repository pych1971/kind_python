def lst(tp='tuple'):
    def inner(ls):
        if tp == 'list':
            return ls
        else:
            return tuple(ls)

    return inner


tp = input()
ls = list(map(int, input().split()))
x = lst(tp)
lst = x(ls)
print(lst)
