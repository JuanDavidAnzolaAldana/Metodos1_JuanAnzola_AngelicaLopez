import numpy
import sympy
import matplotlib.pyplot as plt
def lagrange(pos,points):
    suma=0
    for i in range(len(points)):
        producto=1
        for j in range(len(points)):
            if i!=j:
                producto*=(pos-points[j][0])/(points[i][0]-points[j][0])
        suma+=points[i][1]*producto
    return suma
func=None
f=None
interval=[0,1]
def Interpolar():
    global func
    global f
    global interval
    x=sympy.Symbol("x",real=True)
    ps=numpy.array([[1,0],[2,4],[3,1],[4,2]])
    f=sympy.simplify(lagrange(x,ps))
    func=sympy.lambdify([x],f,numpy)
    interval=[0,5]
    px=numpy.linspace(0,5,100)
    py=func(px)
    plt.title(f)
    plt.plot(px,py)
    plt.scatter(ps[:,0], ps[:,1],color="r")
    plt.show()
def derivada(pos,f,h):
    return (4*f(pos+h)-3*f(pos)-f(pos+2*h))/(2*h)
def derivar():
    if func==None:
        return None
    px=numpy.linspace(interval[0],interval[1],100)
    py=func(px)
    dy=derivada(px,func,0.01)
    plt.plot(px,py)
    plt.plot(px,dy)
    plt.show()
def raiztangente():
    global f
    global func
    global interval
    x=sympy.Symbol("x",real=True)
    f=sympy.sqrt(sympy.tan(x))
    func=sympy.lambdify([x],f,numpy)
    interval=[0.1,1.1]
    px=numpy.linspace(0.1,1.1,100)
    py=func(px)
    plt.title(f)
    plt.plot(px,py)
    plt.show()
def central(pos,f,h):
    return (f(pos+h)-f(pos-h))/(2*h)
def centrar():
    if func==None:
        return None
    px=numpy.linspace(interval[0],interval[1],100)
    py=func(px)
    dy=central(px,func,0.01)
    plt.plot(px,py)
    plt.plot(px,dy)
    plt.show()
raiztangente()
derivar()
centrar()