number = int(input())
s = set()
for i in (1, 2, 3, 5, 7):
    if number % i == 0:
        s.add(i)
print('ДА') if {2, 3, 5} < s else print('НЕТ')
