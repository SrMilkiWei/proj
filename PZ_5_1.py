def generate():  # ввод функции
    length = ""  # ввод переменной
    while len(length) != 1:  # обработка исключений
        try:
            length = input("Введите один абсолютно любой символ ")
        except ValueError:
            print('Неправильно ввели, смотрите условия!')
    print(length * 40)  # умножение строки


generate()  # запуск функции
