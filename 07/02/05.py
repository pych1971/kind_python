def not_even(number):
    return number % 2 != 0


lst = []
src = map(int, input().split())
for i in src:
    if not_even(i):
        lst.append(i)
print(*lst)
