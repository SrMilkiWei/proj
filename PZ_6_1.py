n = input('Введи значение N ')
k = input('Введи значение K ')

while type(n) != int or type(k) != float or False == (1 < k < n):
    try:
        n = int(n)
        k = float(k)
    except ValueError:
        print('Неправильные значения, введите заново!')
        n = input('Введи целое положительное значение N ')
        k = input('Введи значение K, соответствующее условию 1 < K < N ')

a = [i for i in range(0, n)]

for i in a:
    i += k

print('a', a)
