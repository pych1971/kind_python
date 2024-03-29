m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
number1, number2, number3 = map(int, input().split())
note1 = m[number1 - 1] if number1 != 1 and number1 != 4 else '#' + m[number1 - 1]
note2 = m[number2 - 1] if number2 != 1 and number2 != 4 else '#' + m[number2 - 1]
note3 = m[number3 - 1] if number3 != 1 and number3 != 4 else '#' + m[number3 - 1]
print(note1, note2, note3)
