#Calcular todas las raíces reales de: 3x^5+5x^4-x^3
import numpy
import matplotlib.pyplot as plt
import tqdm
deltaDerivate=0.01
deltaInterpolate=0.1
error=0.0000001
def function(x):
    return (3*(x**5))+(5*(x**4))-(x**3)
def sign(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    elif x==0:
        return 0
def bernoulli(a,b):
    while abs(a-b)>error:
        x=a+(b-a)/2
        if sign(function(x))==0:
            return x
        elif sign(function(x))==sign(function(a)):
            a=x
        else:
            b=x
    return a
def todasRaices():
    pasos=numpy.arange(-2,1,deltaInterpolate)
    resultado=[]
    for x in numpy.nditer(pasos):
        x=float(x)
        if sign(function(x))==0:
            resultado.append(x)
        elif sign(function(x+deltaInterpolate))==0:
            x=x
        elif sign(function(x))!=sign(function(x+deltaInterpolate)):
            resultado.append(bernoulli(x,x+deltaInterpolate))
    return resultado
def grafico():
    x0=numpy.array(todasRaices())
    y0=x0.copy()
    for i in range(len(y0)):
        y0[i]=function(x0[i])
    x=numpy.arange(-2,1,0.01)
    y=x.copy()
    for i in range(len(y)):
        y[i]=function(x[i])
    plt.axhline(0,color="r",ls="--")
    plt.plot(x,y)
    plt.scatter(x0, y0,marker="*",c="k")
    plt.show()
while True:
    a=input("""\nProblema 3.10.3 Calcular todas las raíces reales de: 3x^5+5x^4-x^3\nSeleccione:
1. Imprimir en consola los resultados numéricos.\n2. Graficar la función.\n3. salir\n""")
    if a=="1":
        print("las raíces son ",todasRaices())
    elif a=="2":
        grafico()
    elif a=="3":
        print("adios")
        break
    else:
        print("opción inválida")