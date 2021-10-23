n = ''  # введение переменных
s = 0.1
res = 1.1
umn = 1.1
i = 1

while type(n) != int or n <= 0:  # обработка исключений
    try:
        n = int(input('Введите N (целое число больше нуля) '))
    except ValueError:
        print('Неправильно ввели, смотрите условия!')

while n > i:  # цикл умножения
    umn += 0.1
    res *= umn
    i += 1
    if i == n:
        break

print('Произведение сомножителей равно ', res)  # вывод ответа
