def sort_list(func):
    def wrapper(*args, **kwargs):
        res = sorted(func(*args))
        return res

    return wrapper


@sort_list
def get_list(l):
    return list(map(int, l.split()))


lst = get_list(input())
print(*lst)
