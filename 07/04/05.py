def add_tag(txt, tag='h1', up=True):
    if up:
        return f'<{tag.upper()}>{txt}</{tag.upper()}>'
    else:
        return f'<{tag.lower()}>{txt}</{tag.lower()}>'


txt = input()
print(add_tag(txt, 'div'))
print(add_tag(txt, 'div', False))
