def even(number):
    return number % 2 == 0


while (n := int(input())) != 1:
    if even(n):
        print(n)
