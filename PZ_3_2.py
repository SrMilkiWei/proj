a, b, c = '', '', ''  # ввод переменных

while type(a) != float or type(b) != float or type(c) != float:  # обработка исключений
    try:
        a = float(input('Введите значение A '))
        b = float(input('Введите значение B '))
        c = float(input('Введите значение С '))
    except ValueError:
        print('Неправильно ввели, нужно вести число!')

ab = abs(a - b)  # вычисление расстояний между точками
ac = abs(a - c)

if ab > ac:  # вывод ответа
    print('Точка C ближе к точке А, значение С = ', c, ' ,расстояние от А до С = ', ac)
elif ab < ac:
    print('Точка B ближе к точке А, значение B = ', b, ' ,расстояние от А до B = ', ab)
else:
    print('Расстояния от А к С и от A к B равны.')
