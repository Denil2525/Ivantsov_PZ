def Swap(X, Y):
    return Y, X
A = int(1)
B = int(2)
C = int(3)
D = int(4)
X, Y = A, B
X, Y = Swap(X,Y)
A, B = X, Y
X, Y = C, D
X, Y = Swap(X,Y)
C, D = X, Y
X, Y = B, C
X, Y = Swap(X,Y)
B, C = X, Y
print(A)
print(B)
print(C)
print(D)