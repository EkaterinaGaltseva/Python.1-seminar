# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quart = int(input('Введите четверть: '))
if quart == 1:
    print('X range 0 to + infinity, Y range 0 to + infinity')
elif quart == 2:
    print('X range 0 to - infinity, Y range 0 to + infinity')
elif quart == 3:
    print('X range 0 to - infinity, Y range 0 to - infinity')
elif quart == 4:
    print('X range 0 to + infinity, Y range 0 to - infinity')
else:
    print('Ты ввел неверное число. Четвертей всего 4')