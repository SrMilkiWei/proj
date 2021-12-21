j = [6, -21, 97, 3, 2, -14, 9, 8, -60]
k = [7, -99, 21, -8, 64, 25, 8, 66, -2]

f1 = open('data_1.txt', 'w')
f1.write(str(j))
f1.close()

f2 = open('data_2.txt', 'w')
f2.write(str(k))
f2.close()

f3 = open('data_3.txt', 'w', encoding='utf-8')
f3.write('Элементы первого и второго файлов:\n')
f3.write(str(j))
f3.write('\n')
f3.write(str(k))

f3.write("\nКоличество элементов первого файла: ")
f3.write(str(len(j)))

f3.write("\nКоличество элементов второго файла: ")
f3.write(str(len(k)))

f3.write("\nКоличество элементов, общих для двух файлов:")

j = set(j)
k = set(k)
f3.writelines(str(len(j & k)))

f3.write("\nКоличество чётных элементов первого файла: ")

b = 0

for i in j:
    x = i % 2
    if x == 0:
        b += 1
    else:
        pass

f3.write(str(b))

f3.write("\nКоличество нечётных элементов второго файла: ")

b = 0

for i in j:
    x = i % 2
    if x == 1:
        b += 1
    else:
        pass

f3.write(str(b))
