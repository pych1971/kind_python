cmd = input()

match cmd:
    case command if command.lower() == 'top':
        print(f'Команда {command.lower()}')
    case command if command.lower() == 'bottom':
        print(f'Команда {command.lower()}')
    case command if command.lower() == 'right':
        print(f'Команда {command.lower()}')
    case command if command.lower() == 'left':
        print(f'Команда {command.lower()}')
    case _:
        print('Неверная команда')
