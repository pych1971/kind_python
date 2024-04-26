def get_dict(func):
    def wrapper(*args, **kwargs):
        s1, s2 = args
        l1, l2 = func(s1, s2)
        d = dict()
        for key, word in enumerate(l1):
            d[word] = l2[key]
        return d

    return wrapper


@get_dict
def get_lists(l1, l2):
    return list(l1.split()), list(l2.split())


d = get_lists(input(), input())
print(*sorted(d.items()))
