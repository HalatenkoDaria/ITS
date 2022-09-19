import math
x=float(input("x="))
def f(x):
    if x >= 3:
        return math.sin(x)
    if x >= 0 and x < 3:
        return math.cos(x)
    else:
        return math.tan(x)
print(f(x))