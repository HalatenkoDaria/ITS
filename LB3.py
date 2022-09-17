import sys
a=float(sys.argv[1])
x=a%10
y=a//100
z=a//10%10
c=(x+y+z)/3
print(c)