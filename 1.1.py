from math import sqrt, sin
def f(x, y):
    p1 = sqrt((x**7 - 78*y**8) / (x**2+y**5-38)) + x**7
    p2 = 16*y**2 - (sin(y) + y**8 - 72) / (x - x**7)
    return p1 - p2
print(f(-56, -23))
print(f(31, 1))