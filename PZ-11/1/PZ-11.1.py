l = '1 -1 2 -2 3 -3 4 -4 5 -5'
f3 = open('data_3.txt', 'w', errors='ignore')
f3.writelines(l)
f3.close()
f4 = open('data_4.txt', 'w', errors='ignore')
f4.write('Исходные данные: ')
f4.writelines(l)
f4.close()
f3 = open('data_3.txt', errors='ignore')
k = f3.read()
k = k.split()
n = l.split()
inmax = k
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()
f3 = open('data_3.txt', errors='ignore')
t = 0
for i in range(len(k)):
    if k[i] < 0:
        t += 1
f3.close()
f1 = open('text18-9.txt', errors='ignore')
l2 = f1.readlines()
l2[0], l2[3] = l2[3], l2[0]
f1.close()
f4 = open('data_4.txt', 'a', errors='ignore')
f4.write('\n')
print('Количество элементов:', len(k), file=f4)
print('Индекс последнего максимального элемента:', inmax.index(max(inmax)), file=f4)
print('Меняем местами первую и последнюю трети:', l2, file=f4)
f4.close()