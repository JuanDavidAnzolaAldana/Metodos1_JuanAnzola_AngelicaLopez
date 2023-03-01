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
x=sympy.Symbol("x",real=True)
func=None
f=None
interval=[0,1]
def Interpolar():
    global func
    global f
    global interval
    ps=numpy.array([[0,1],[1,2],[2,-1],[3,-2],[4,5]])
    f=sympy.simplify(lagrange(x,ps))
    func=sympy.lambdify([x],f,numpy)
    interval=[-1,5]
    px=numpy.linspace(-1,5,100)
    py=func(px)
    plt.title(f)
    plt.plot(px,py)
    plt.scatter(ps[:,0], ps[:,1],color="r")
    plt.show()
def derivada(pos,f,h):
    return (4*f(pos+h)-3*f(pos)-f(pos+2*h))/(2*h)
def derivar():
    if func==None:
        print("Defina una función primero.")
        return None
    px=numpy.linspace(interval[0],interval[1],100)
    py=func(px)
    dy=derivada(px,func,0.01)
    plt.plot(px,py)
    plt.plot(px,dy)
    plt.title(str(f)+"derecha")
    plt.show()
def raiztangente():
    global f
    global func
    global interval
    f=sympy.sqrt(sympy.tan(x))
    func=sympy.lambdify([x],f,numpy)
    interval=[0.1,1.1]
    px=numpy.linspace(0.1,1.1,100)
    py=func(px)
    plt.title(str(f))
    plt.plot(px,py)
    plt.show()
def central(pos,f,h):
    return (f(pos+h)-f(pos-h))/(2*h)
def centrar():
    if func==None:
        print("Defina una función primero.")
        return None
    px=numpy.linspace(interval[0],interval[1],100)
    py=func(px)
    dy=central(px,func,0.01)
    plt.title(str(f)+"central")
    plt.plot(px,py)
    plt.plot(px,dy)
    plt.show()
def analtica():
    if func==None:
        print("Defina una función primero.")
        return None
    px=numpy.linspace(interval[0],interval[1],100)
    py=func(px)
    der=sympy.lambdify([x],sympy.diff(f,x))
    dy=central(px,func,0.01)
    dy2=derivada(px,func,0.01)
    dy3=der(px)
    plt.title(str(f)+"Comparación")
    plt.plot(px,py,label="Función")
    plt.plot(px,dy3,label="Derivada analítica")
    plt.plot(px,dy2,label="Derivada derecha")
    plt.plot(px,dy,label="Derivada central")
    plt.legend()
    plt.show()
def comparacion():
    if func==None:
        print("Defina una función primero.")
        return None
    px=numpy.linspace(interval[0],interval[1],100)
    der=sympy.lambdify([x],sympy.diff(f,x))
    dy=numpy.abs(central(px,func,0.01)-der(px))
    dy2=numpy.abs(derivada(px,func,0.01)-der(px))
    plt.title(str(f)+"Error")
    plt.plot(px,dy2,label="Derivada derecha")
    plt.plot(px,dy,label="Derivada central")
    plt.legend()
    plt.show()
while True:
    a=input("""\nProblema 3.7.8 derivada derecha\nSeleccione:
1. Definir función interpolando conjunto soporte.\n2. Definir función raiz de tangente.
3. Calcular derivada derecha.\n4. Calcular derivada central.\n5. Comparar derivada analítica, derecha y central
6. Graficar el error.\n7. Salir.\n""")
    if a=="1":
        Interpolar()
    elif a=="2":
        raiztangente()
    elif a=="3":
        derivar()
    elif a=="4":
        centrar()
    elif a=="5":
        analtica()
    elif a=="6":
        comparacion()
    elif a=="7":
        print("adios")
        break
    else:
        print("opción inválida")