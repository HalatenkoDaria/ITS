import math
a=float(input("a="))
b=float(input("b="))
h=float(input("h="))
x=a
y=0.0
while (x<=b):
    y=3-math.log(math.fabs(x-6),math.e)+math.cos(x)
    y=round(y,4)
    print(x," ",y)
    x=x+h
    x=round(x,1)
    