word = input()
key = 123
res = ''
for x in word:
    res += chr(ord(x) ^ key)
print(res)
