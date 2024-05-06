def return_primitive(number=2):
    while True:
        for i in range(2, round(number ** 0.5) + 1):
            if number % i == 0:
                number += 1
                break
        else:
            yield number
            number += 1


p = return_primitive()
for i in range(20):
    print(next(p), end=' ')
