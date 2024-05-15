def get_add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and type(a) != bool and type(
            b) != bool or isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        return None
