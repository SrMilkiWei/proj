f1 = open("text18-29.txt", "rt", encoding='utf-8')
j = f1.readlines()
for i in j:
    print(i, end='')

print("\nКоличество символов в тексте - ", len(str(j)))
f1.close()

f1 = open("text18-29.txt", "rt", encoding='utf-8')
f2 = open("text18-29_new.txt", 'w', encoding='utf-8')

f2.write(j[0])
f2.write(j[1])
f2.write(j[6])
f2.write('\n')
f2.write(j[2])
f2.write(j[3])
f2.write(j[4])
f2.write(j[5])

print(f2)
