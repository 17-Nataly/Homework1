x = int(input('Введите координату точки x не равную 0:'))
y = int(input('Введите координату точки y не равную 0:'))
if x == 0 or y == 0:
    print('Введены ошибочные координаты!')
elif x > 0 and y < 0:
    print('сектор 4')
elif x > 0 and y > 0:
    print('сектор 1')
elif x < 0 and y < 0:
    print('сектор 3')
else:
    print('сектор 2')