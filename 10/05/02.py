t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]
match book:
    case (_, str(author), str(name)) if len(author) >= 6 and len(name) >= 10:
        print('Yes')
    case (_, str(author), str(name), float(price)) if len(author) >= 6 and price > 0:
        print('Yes')
    case (_, str(author), str(name), int(year)) if year >= 2020:
        print('Yes')
    case (_, str(author), str(name), float(price), int(year)) if price > 0 and year >= 2020:
        print('Yes')
    case _:
        print('No')
