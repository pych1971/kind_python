expression = input()
while ' ' in expression:
    expression = expression.replace(' ', '')
expression_list = expression.split('+')
result = 0
for i in range(len(expression_list)):
    expression_list[i] = list(map(int, expression_list[i].split('-')))
    result += expression_list[i][0] - sum(expression_list[i][1:])
print(result)
