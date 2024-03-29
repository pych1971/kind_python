str = input()
while '--' in str:
    str = str.replace('--', '-')
print(str)
