def counter_add():
    def inner(k):
        k += 5
        return k

    return inner


k = int(input())
cnt = counter_add()
print(cnt(k))
