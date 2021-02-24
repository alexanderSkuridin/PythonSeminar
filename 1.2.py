def f(x):
    if x < 55:
        return 78*x*x + x**4 + 93
    elif x < 104:
        return x**6 - x/15 - 20
    elif x < 200:
        return 98*(x**4 + x**5 -2)**7
    else:
        return 67*x**4 - x
print(f(-1))
print(f(230))