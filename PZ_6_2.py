n = int(input("Введите длину списка "))

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print('Длина списка должна быть целочисленной! ')
        n = int(input('Введите правильную длину списка '))

a = [i for i in range(0, n)]
b = a[1::2] + a[0::2]

print('Ваш результат:\n', b)
