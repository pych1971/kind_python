a, b = map(int, input().split())
gen = (abs(x) for x in range(a, b + 1))
for i in range(5):
    print(next(gen))
