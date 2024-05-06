import random
from string import ascii_lowercase, ascii_uppercase

# установка зерна датчика случайных чисел (не менять)
random.seed(1)


# здесь продолжайте программу
def generate_email(N):
    chars = ascii_lowercase + ascii_uppercase
    ps = ''
    for i in range(N):
        ps += chars[random.randint(0, len(chars))]
    yield ps + '@mail.ru'


N = int(input())
for i in range(5):
    print(next(generate_email(N)))
