from math import fabs

def f(n):
    if n == 0:
        return 10
    elif n == 1:
        return 8
    else:
        return fabs(f(n-1)) + f(n-2)**2/72
print(f(4))
print(f(15))