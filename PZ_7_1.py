s = str(input('Введите что угодно в строку S\n'))
c = str(input('Введите проверяемый символ С '))
so = str(input('Введите вставляемую строку\n'))

s_new = s.replace(c, c + so)
print('Полученная строка:\n', s_new)
