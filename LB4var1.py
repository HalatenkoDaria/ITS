import math
x=float(input("x="))
def f(x):
    return 3*math.tan(x)/(math.log(math.cos(x),math.e)+4)+(math.fabs(x-math.pow(x,2)))
print(f(x))