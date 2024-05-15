notes_source = 'до, ре, ми, фа, соль, ля, си'.split(', ')
notes = input().split()
print(*sorted(notes, key=lambda x: notes_source.index(x)))
