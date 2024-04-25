def tag():
    def txt(s):
        return f'<h1>{s}</h1>'

    return txt


s = input()
t = tag()
print(t(s))
