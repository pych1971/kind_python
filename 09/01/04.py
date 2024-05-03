a = int(input())
gen1 = (abs(x) for x in range(0 - a, a + 1))
gen2 = (x ** 3 for x in gen1)
for i in range(4):
    print(next(gen2), end=' ')
