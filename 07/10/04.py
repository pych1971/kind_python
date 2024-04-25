def tag(t):
    def txt(s):
        return f'<{t}>{s}</{t}>'

    return txt


s = input()
t = input()
txt = tag(s)
print(txt(t))
