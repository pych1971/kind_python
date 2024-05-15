import importlib.util
import sys

# считывание списка из входного потока (переменную lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
zv = 'рядовой, сержант, старшина, прапорщик, лейтенант, капитан, майор, подполковник, полковник'.split(', ')
lst = sorted([i.split('=') for i in lst_in], key=lambda x: zv.index(x[1]))
