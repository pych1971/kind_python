number = input()
result = number[0:2]
for i in range(2, len(number)):
    if '0' <= number[i] <= '9':
        result += 'x'
    else:
        result += number[i]
if result == '+7(xxx)xxx-xx-xx':
    print('ДА')
else:
    print('НЕТ')
