import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))


# здесь продолжайте программу (используйте список строк lst_in)
def return_3(goods):
    prices = sorted(goods)
    goods_3 = []
    for i in range(3):
        goods_3.append(goods[prices[i]])
    return goods_3


goods = dict([[int(item.split(':')[1]), item.split(':')[0]] for item in lst_in])
print(*return_3(goods))
