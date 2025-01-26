#Описать функцию Swap(X, Y), меняющую содержимое переменных X и Y (X и Y — 
#вещественные параметры, являющиеся одновременно входными и выходными). С 
#ее помощью для данных переменных A, B, C, D последовательно поменять 
#содержимое следующих пар: A и B, C и D, B и C и вывести новые значения A, B, C, D.
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
