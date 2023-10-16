from math import *
x,y=map(float,input().split())
f=(1/(x+2/(x*x)+3/(x*x*x))+exp(x*x+3*x))/(atan(x+y)+fabs(5+x)**2)-cos(y*y+(x*x)/2)**2
print(f'{f:.2f}')
