txt = [i.lower() for i in input().split()]
set_txt = {i for i in txt}
dict_txt = {i: txt.count(i) for i in set_txt}
print(dict_txt['и']) if 'и' in dict_txt.keys() else print(0)
