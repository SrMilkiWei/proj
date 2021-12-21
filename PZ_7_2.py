s = str(input('Введите строку, содержащую хотя бы один пробел'))

p1 = s.find(' ')
p2 = s.rfind(' ')
pL = len(s)

if p1 + p2 == pL:
    print("Ваш результат: ")
else:
    print('Ваш результат: \n', s[p1:p2])
