import sympy
import numpy
x=sympy.Symbol("x",real=True)
def func(eq,pos):
    val=sympy.lambdify([x],eq)(pos)
    if numpy.sum(numpy.isnan(val)):
        raise Exception("not a number")
    return val
def legendre(n):
    f=(x**2-1)**n
    for i in range(n):
        f=sympy.diff(f,x)
    return sympy.simplify(f/(2**n*numpy.math.factorial(n)))
def grado(pol):
    gra=0
    try:
        pol-=func(pol,0)
    except:
        return -1
    while pol!=0 and gra<100:
        try:
            pol/=x
            pol=sympy.simplify(pol)
            pol-=func(pol,0)
            gra+=1
        except:
            return -1
    if pol==0:
        return gra
    return -1
def integral(eq,gra):
    deg=int(numpy.ceil((gra+1.0)/2))
    points,weighs=numpy.polynomial.legendre.leggauss(deg)
    return numpy.sum(weighs*func(eq,points))
def descomponer():
    polinomio=3+5*x+x**2
    print("El polinomio en la base estándar es ",polinomio)
    grad=grado(polinomio)
    base=[0]*(grad+2)
    for i in range(len(base)):
        base[i]=legendre(i)
    lista=[]
    for i in range(len(base)):
        lista.append(integral(base[i]*polinomio,i+grad)/integral(base[i]**2,2*i))
    cadena="El polinomio en la base de Legendre es: "
    for i in range(len(lista)):
        cadena+=str(round(lista[i]*3))+"/3 p"+str(i)+"(x) + "
    print(cadena[0:-1])
while True:
    a=input("""\nProblema 3.14.14 Base de Legendre\nSeleccione:
1. Descomponer polinomio en la base de Legendre.\n2. Salir.\n""")
    if a=="1":
        descomponer()
    elif a=="2":
        print("adios")
        break
    else:
        print("opción inválida")