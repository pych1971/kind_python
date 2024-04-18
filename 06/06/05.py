import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
lst_authors = {x.split(': ')[0] for x in lst_in}
d = {author: {i.split(': ')[1] for i in lst_in if i.split(': ')[0] == author} for author in lst_authors}
