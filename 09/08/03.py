def get_even_sum(it):
    return sum(filter(lambda x: type(x) is int and x % 2 == 0, it))
