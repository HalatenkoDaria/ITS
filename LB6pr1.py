import math
a=float(input("a="))
b=float(input("b="))
h=float(input("h="))
x=a
y=0.0
for i in range(100):
    y=3-math.log(math.fabs(x-6),math.e)+math.cos(x)
    print(i," ",x," ",y)
    x=x+h
    x=round(x,1)
    if x>b:
        break
