def merge_two_list(a, b):
    s = []
    while len(a) >= 1 or len(b) >= 1:
        if len(a) == 0:
            s.append(b[0])
            del b[0]
        elif len(b) == 0:
            s.append(a[0])
            del a[0]
        elif a[0] <= b[0]:
            s.append(a[0])
            del a[0]
        elif b[0] <= a[0]:
            s.append(b[0])
            del b[0]
    return s


def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_list(left, right)

print(*merge_sort(list(map(int, input().split()))))