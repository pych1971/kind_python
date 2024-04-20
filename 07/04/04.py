def add_tag(txt, tag='h1'):
    return f'<{tag}>{txt}</{tag}>'


txt = input()
print(add_tag(txt))
print(add_tag(txt, 'div'))
