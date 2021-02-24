from math import log

def f(n, m):
    s1 = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            s1 += (i**7 - 78*j**8)
    s2 = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            s2 += (log(j) - j**8)
    result = 41*s1 +47*s2
    return result

print(f(31, 64))
print(f(68, 72))