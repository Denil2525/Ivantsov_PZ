n = 6
c1,c2 = "х","а"
t,r = 0,1
list = []
while t != n:
    if r == 1:
        list.append(c1)
        r = 2
    elif r == 2:
        list.append(c2)
        r = 1
    t += 1
print(*list)