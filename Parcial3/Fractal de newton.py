import sympy
from sympy import I
import matplotlib.pyplot as plt
import numpy
import tqdm
#Punto a
x=sympy.Symbol("x",real=True)
y=sympy.Symbol("y",real=True)
#Punto b
z=x+(y*I)
#Punto c
f=z**3-1
#Punto d, f
func=sympy.lambdify([x,y],f)
def function(x,y):
    num=func(x,y)
    return numpy.array([sympy.re(num),sympy.im(num)])
#Punto e
j00=sympy.diff(sympy.re(f),x)
j01=sympy.diff(sympy.re(f),y)
j10=sympy.diff(sympy.im(f),x)
j11=sympy.diff(sympy.im(f),y)
jacobiano=sympy.matrices.Matrix([[j00,j01],[j10,j11]])
print(jacobiano)
jac=sympy.lambdify([x,y],jacobiano)
#Punto g
def newtonRaphson(punto,f,j):
    delta=numpy.array((1,1))
    i=0
    while numpy.sum(delta**2)**(1/2)>0.0000001 and i<1000:
        i+=1
        jac=j(punto[0],punto[1])
        inv=numpy.linalg.inv(jac)
        delta=numpy.zeros([2])
        for i in range(2):
            delta[i]=numpy.sum(inv[i]*f(punto[0],punto[1]))
        punto-=delta
    return punto
#Punto h
print(newtonRaphson(numpy.array([0.5,0.5]), function, jac))
#Punto i
x0=numpy.linspace(-1,1,300)
y0=numpy.linspace(-1,1,300)
X,Y=numpy.meshgrid(x0,y0)
#Punto j
Z=numpy.zeros([300,300],numpy.int64)
for i in tqdm.tqdm(range(len(X))):
    for j in range(len(X[0])):
        try:
            resultado=newtonRaphson(numpy.array([X[i,j],Y[i,j]]), function, jac)
        except Exception as e:
            resultado=numpy.array([0,0])
            priint(e)
            
        d0=numpy.array([-1/2,(3**(1/2))/2])-resultado
        d1=numpy.array([-1/2,-(3**(1/2))/2])-resultado
        d2=numpy.array([1,0])-resultado
        if (numpy.sum(d0**2)**(1/2)<0.1):
            Z[i,j]=20
        if (numpy.sum(d1**2)**(1/2)<0.1):
            Z[i,j]=100
        if (numpy.sum(d2**2)**(1/2)<0.1):
            Z[i,j]=222
#Punto k
plt.imshow(Z,cmap="coolwarm",extent=[-1,1,-1,1])
plt.show()