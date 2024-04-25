def get_path(N, s=0):
    if N <= 2:
        s = N
    else:
        s = get_path(N - 1) + get_path(N - 2)
    return s


print(get_path(int(input())))
