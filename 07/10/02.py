def counter_add(n):
    def inner(k):
        nonlocal n
        return k + n

    return inner


cnt = counter_add(2)
k = int(input())
print(cnt(k))
