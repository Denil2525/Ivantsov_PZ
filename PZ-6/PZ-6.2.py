import random

N = random.randrange(2, 21)  # N = 15
a = [random.randrange(1, 10) for i in range(N)]
print("N = ", N)
print("Список: ",a)
k = 0
flag = True
for i in range(1, N):
    if a[i-1] > a[i]:
        if flag:
            k += 1
            flag = False
    else:
        flag = True
print("Монотонные убывающие участки:", k)