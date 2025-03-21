l = ['1 -1 2 -2 3 -3 4 -4 5 -5']
f3 = open('data_3.txt', 'w')
f3.writelines(l)
f3.close()
f4 = open('data_4.txt', 'w')
f4.write('Исходные данные: ')
f4.writelines(l)
f4.close()
f3 = open('data_3.txt')
k = f3.read()
k = k.split()
n = k
n.sort(key=None, reverse=True)
inmax = n
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()
f3 = open('data_3.txt')
inmax, t = 0, 0
for i in range(len(k)):
    if k[i] < 0:
        t += 1
f4 = open('data_4.txt', 'a')
f4.write('\n')
print('Количество элементов:', len(k), file=f4)
print('Индекс последнего максимального элемента:', inmax, file=f4)
f4.close()