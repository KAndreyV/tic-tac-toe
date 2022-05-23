#Приветствие и правила
def rules():
    print('Добро пожаловать в игру Крестики-нолики!')
    print('Правила нашей игры (формат ввода): x y')
    print('x - номер строки')
    print('y - номер столбца')
    print('--------')

#Создаем и показываем поле
def show_field():
    print()
    print('Игровое поле)')
    print('   0 1 2')
    for i in range(3):
        print(f'{i}  {field[i][0]} {field[i][1]} {field[i][2]}')
    print()

#Правильность ввода
def coordinates():
    while True:
        step = input('Ваш ход: ').split()

        if len(step) != 2:
            print('Введите 2 координаты!')
            continue

        x, y = step

        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа!')
            continue

        x, y = int(x), int(y)

        if x > 2 or x < 0 or y > 2 or y < 0:
            print('Недопустимые значения координат!')
            continue

        if field[x][y] != '_':
            print('Ячейка занята!')
            continue

        print(x, y)
        return x, y

#Проверка выигрыша
def winner():
    sr = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
          ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 1), (2, 2)),
          ((0, 2), (1, 1), (2, 1))]
    for r in sr:
        s = []
        for v in r:
            s.append(field[v[0]][v[1]])
        if s == ['x', 'x', 'x']:
            print('Крестик победил!')
            return True
        if s == ['0', '0', '0']:
            print('Нолик победил!')
            return True
    return False

rules()
field = [['_'] * 3 for _ in range(3)]
i = 0

while True:
    show_field()
    i += 1

    if i % 2 == 1:
        print('Ходит крестик')
        x, y = coordinates()
        field[x][y] = 'x'
    else:
        print('Ходит нолик')
        x, y = coordinates()
        field[x][y] = '0'

    show_field()

    if winner() is True:
        break

    if i == 9:
        print('Ничья!')
        break