import sympy
import numpy
import matplotlib.pyplot as plt
x=sympy.Symbol("x",real=True)
def hermite(n):
    f=sympy.exp(-x**2)
    for i in range(n):
        f=sympy.diff(f,x)
    f/=sympy.exp(-x**2)
    f=sympy.simplify(f)
    return(-1)**n*f
def func(eq,pos):
    val=sympy.lambdify([x],eq)(pos)
    if numpy.sum(numpy.isnan(val)):
        raise Exception("not a number")
    return val
def newton(eq,point):
    err=1
    while abs(err)>0.00000001:
        try:
            err=func(eq,point)/func(sympy.diff(eq,x),point)
        except:
            return None
        point-=err
    return point
def PuntosPesos(n):
    point=-6.0
    puntos=[]
    while len(puntos)<n and point<=6:
        punto=newton(base[n],point)
        boolean=True
        for i in range(len(puntos)):
            if punto==None:
                boolean=False
                break
            if abs(puntos[i]-punto)<0.00000002:
                boolean=False
                if abs(func(base[n],punto))<abs(func(base[n],puntos[i])):
                    puntos[i]=punto
                break
        if boolean:
            puntos.append(punto)
            pass
        point+=0.25
    puntos=numpy.array(puntos)
    if len(puntos)!=n:
        print(len(puntos))
        raise Exception("Muy pocos puntos")
    pesos=((2**(n-1))*numpy.math.factorial(n)*(numpy.pi**(1/2)))/((n**2)*(func(base[n-1],puntos)**2))
    return puntos, pesos
def interfaz():
    for i in range(len(base)):
        print("El "+str(i)+"-avo polinomio de Hermite es: "+str(base[i]))
        print("Los ceros de este polinomio son: ")
        p,P=PuntosPesos(i)
        print(p)
        print("Y sus pesos respectivos son: ")
        print(P)
def oscilador():
    funcion=((x**2)*(base[1]**2))/(2*(numpy.pi**(1/2)))
    puntos, pesos=PuntosPesos(3)
    integral=numpy.sum(pesos*func(funcion,puntos))
    return integral
base=[]
for i in range(20):
    base.append(hermite(i))
while True:
    a=input("""\nProblema 3.14.18 Cuadratura de Hermite\nSeleccione:
1. Hallar los ceros de los 20 primeros polinomios de Hermite.\n2. Calcular el valor cuadrático medio de la posición del oscilador harmónico cuántico.
3. Salir.\n""")
    if a=="1":
        interfaz()
    elif a=="2":
        print("El valor cuadrático medio de la posición del oscilador armónico cuántico es:")
        print(oscilador())
    elif a=="3":
        print("adios")
        break
    else:
        print("opción inválida")