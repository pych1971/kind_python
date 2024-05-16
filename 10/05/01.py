t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]
match book:
    case (_, str(author), str(name)):
        print('Yes')
    case (_, str(author), str(name), float(price)):
        print('Yes')
    case (_, str(author), str(name), int(year)):
        print('Yes')
    case (_, str(author), str(name), float(price), int(year)):
        print('Yes')
    case _:
        print('No')
