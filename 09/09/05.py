def is_free(lst):
    return any(any(i == '#' for i in j) for j in lst)
