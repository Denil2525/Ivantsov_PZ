l = ['-99 6 12 -36 20 45 100 -15']
f3 = open('data_3.txt', 'w')
f3.writelines(l)
f3.close()
f4 = open('data_4.txt', 'w')
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()
f3 = open('data_3.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()
f3 = open('data_3.txt')
max, t = 0, 0
for i in range(len(k)):
    max = max if max > k[i] else k[i]
    if k[i] < 0:
        t += 1
f4 = open('data_4.txt', 'a')
f4.write('\n')
print('Количество элементов:', len(k), 'Максимальный элемент:', max, file=f4)
f4.close()