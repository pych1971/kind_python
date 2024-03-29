word = input()
msg = "палиндром" if word.upper() == word[::-1].upper() else "не палиндром"
print(msg)
