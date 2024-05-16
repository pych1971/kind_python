def get_data(value):
    match value:
        # здесь продолжайте программу
        case int() as x if x > 0:
            return x
        case float() as x if -100 <= x <= 100:
            return x
        case str() as x:
            return x

    return None
