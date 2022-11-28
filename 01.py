num = int(input('Введите номер дня недели:'))
if num == 6 or num == 7:
    print('Да, выхоной!')
elif num < 6 and num > 0:
    print('Нет, будний день')
else:
    print('Это ошибочный номер')