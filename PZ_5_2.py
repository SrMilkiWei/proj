a = input('Введите любое значение a ')
b = input('Введите любое значение b ')
c = input('Введите любое значение c ')
d = input('Введите любое значение d ')


def swap(x, y):
    global a
    global b
    global c
    global d
    x, y = y, x
    return x, y


a, b = swap(a, b)
c, d = swap(c, d)
b, c = swap(b, c)

print('a = ', a, '; b = ', b, '; c = ', c, '; d =', d)
