def get_biggest_city(*args):
    max_city_chars = 0
    max_city = ''
    for city in args:
        if len(city) > max_city_chars:
            max_city_chars = len(city)
            max_city = city
    return max_city
