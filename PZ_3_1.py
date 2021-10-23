x = ''  # ввод переменных
y = ''
x1 = ''
y1 = ''
x2 = ''
y2 = ''

while type(x) != float or type(y) != float or type(x1) != float or type(x2)\
        != float or type(y1) != float or type(y2) != float:  # обработка исключений
    try:
        x = float(input('Введите значение x '))
        y = float(input('Введите значение y '))
        x1 = float(input('Введите значение x1 '))
        y1 = float(input('Введите значение y1 '))
        x2 = float(input('Введите значение x2 '))
        y2 = float(input('Введите значение y2 '))
    except ValueError:
        print('Неправильно ввели, нужно вести число!')

if x1 < x < x2 and y1 < y < y2:
    print('Высказывание истинно')
else:
    print('Высказывание ложно')
