lst_tmp = [[x] if i % 2 == 0 else [int(x)] for i, x in enumerate(input().split())]
lst = [lst_tmp[i] + lst_tmp[i + 1] for i in range(len(lst_tmp)) if i % 2 == 0]
print(lst)
