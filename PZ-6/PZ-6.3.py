import random
import math

N = 20
class Tochka:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
def main():
    random.seed()
    A = [Tochka(random.randint(0, 49), random.randint(0, 49)) for _ in range(N)]
    b = Tochka(random.randint(0, 49), random.randint(0, 49))
    print(f"Tochka B ({b.x}, {b.y})\n")
    for i in range(N):
        print(f"Tochka {i + 1} ({A[i].x}, {A[i].y})")
    min_distance = math.sqrt((A[0].x - b.x) ** 2 + (A[0].y - b.y) ** 2)
    j = 0
    for i in range(1, N):
        temp_distance = math.sqrt((A[i].x - b.x) ** 2 + (A[i].y - b.y) ** 2)
        if temp_distance < min_distance:
            min_distance = temp_distance
            j = i
    print(f"Наиближайшая точка A к точке B - Точка {j + 1} ({A[j].x}, {A[j].y})")
main()

