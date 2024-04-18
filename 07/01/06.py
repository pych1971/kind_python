def check(address):
    sum = 0
    for i in address:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z' or '0' <= i <= '9' or i == '_':
            sum += 1
    if '@' in address and '.' in address:
        sum += 2
    if sum == len(address):
        print('ДА')
    else:
        print('НЕТ')


check(input())
