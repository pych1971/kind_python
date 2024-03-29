word = input()
if word.upper() == word[::-1].upper():
    print('ДА')
else:
    print('НЕТ')
