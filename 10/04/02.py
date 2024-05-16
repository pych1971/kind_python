def get_data(value):
    match value:
        # здесь продолжайте программу
        case int() | float() | str() as res:
            return res

    return None
