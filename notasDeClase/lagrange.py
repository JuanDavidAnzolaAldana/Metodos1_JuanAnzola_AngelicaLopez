import numpy
import sympy
import matplotlib.pyplot as plt
x=numpy.array([1,2,3,4,5])
y=numpy.array([-3.4,-5.6,0,3,3.5])
def Lagrange(x0,j):
    prod=1.0
    for i in range(len(x)):
        if i!=j:
            prod *= (x0 - x[i])/(x[j]-x[i])
    return prod
def Interpolate(x0):
    sum=0
    for i in range(len(x)):
        sum+=y[i]*Lagrange(x0,i)
    return sum
def derivate(func,p,h):
    return (func(p+h)-func(p-h))/h
def criticos(func,point,h):
    err=10
    r=point
    while abs(err)>0.0001:
        err=derivate(func,r,h)/seconderivate(func, r, h)
        r=r-err
        print(r)
    return r
    
x0=numpy.linspace(1,6,100)
y0=Interpolate(x0)
y1=derivate(Interpolate,x0,0.001)
eq=sympy.simplify(Interpolate(sympy.Symbol("x",real=True)))
print((eq))
min=criticos(Interpolate,2.0,0.001)
plt.plot(x0,y0)
plt.plot(x0,y1)
plt.scatter(x,y,c="r")
plt.scatter(min, Interpolate(min))
plt.title(eq)
plt.show()