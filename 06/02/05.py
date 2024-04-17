things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

N = int(input()) * 1000
while N >= 0 and things != {}:
    thing_max = max(things.values())
    for key, value in things.items():
        if value == thing_max and thing_max > N:
            things.pop(key)
            break
        elif value == thing_max and thing_max <= N:
            print(key, end=' ')
            N -= value
            things.pop(key)
            break
