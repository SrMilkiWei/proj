n = int(input("Введите длину списка "))
k = int(input('Введите количество сдвигов вправо '))

while type(n) != int or type(k) != int:
    try:
        n = int(n)
        k = int(k)
    except ValueError:
        print('Длина списка должна быть целочисленной, как и количество сдвигов! ')
        n = int(input('Введите правильную длину списка '))
        k = int(input('Введите правильно количество сдвигов вправо'))

if 1 < k < n:
    a = [i for i in range(0, n)]
    a = a[-k:] + a[:-k]
    print('Результат сдвига:\n', a)
else:
    print('Несоответствие условию 1 < K < N!')
