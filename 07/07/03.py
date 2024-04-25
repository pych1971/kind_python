# ввод числа N
N = int(input())


# здесь задается функция fib_rec (переменную N не менять!)
def fib_rec(N, f=[]):
    if len(f) < 2:
        f += [1, 1]
    if len(f) < N:
        f.append(f[-1] + f[-2])
        fib_rec(N, f)
    return f


print(fib_rec(N))
