def get_data_fig(*args, **kwargs):
    params = ('type', 'color', 'closed', 'width')
    res = (sum(args),)
    for p in params:
        if p in kwargs:
            res += (kwargs[p],)
    return res
