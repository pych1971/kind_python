def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


# здесь продолжайте программу
lst_src = list(map(int, input().split()))
lst = filter_lst(lst_src)
print(*lst)
lst = filter_lst(lst_src, lambda x: x < 0)
print(*lst)
lst = filter_lst(lst_src, lambda x: x >= 0)
print(*lst)
lst = filter_lst(lst_src, lambda x: 3 <= x <= 6)
print(*lst)
