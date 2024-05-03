from string import ascii_lowercase

gen = (x + y for x in ascii_lowercase for y in ascii_lowercase)
for i in range(50):
    print(next(gen), end=' ')
