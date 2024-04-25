d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]


# здесь продолжайте программу
def get_line_list(d, a=[]):
    for element in d:
        if type(element) == list:
            get_line_list(element, a)
        else:
            a.append(element)
    return a


print(get_line_list(d))
