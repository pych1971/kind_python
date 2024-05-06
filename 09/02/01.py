# ввод значения N (эту переменную не менять)
N = int(input())


# здесь продолжайте программу


def get_sum(N):
    sum = 0
    for i in range(1, N + 1):
        sum += i
        yield sum
