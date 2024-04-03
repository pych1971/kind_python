lst_in = list(map(int, input().split()))
lst = [[lst_in[i] for i in range(j, j + (int(len(lst_in) ** (0.5))))] for j in
       range(0, len(lst_in), int(len(lst_in) ** (0.5)))]
print(lst)
