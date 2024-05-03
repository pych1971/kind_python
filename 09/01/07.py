import numpy

a, b = map(int, input().split())
gen = (0.5 * pow(x, 2) - 2.0 for x in numpy.arange(a, b + 0.01, 0.01))
for i in range(20):
    print(round(next(gen), 2), end=' ')
