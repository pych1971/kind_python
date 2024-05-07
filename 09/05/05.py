# считывание строки в переменную s (эту переменную в программе не менять)
s = input()

# здесь продолжайте программу
symbols = []
indexes = []
for index, symbol in enumerate(s):
    if index < 10:
        symbols.append(symbol)
        indexes.append(index)
lst = list(zip(symbols, indexes))
