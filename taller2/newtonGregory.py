import os
import urllib.request
import numpy
import pandas
import sympy
import matplotlib.pyplot as plt
x=sympy.Symbol("x",real=True)
def cargar():
    if not os.path.exists(os.path.dirname(__file__)+"/Data"):
        os.mkdir(os.path.dirname(__file__)+"/Data")
    if not os.path.exists(os.path.dirname(__file__)+"/Data/newton.csv"):
        url="https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/InterpolacionNewtonNoequi.csv"
        urllib.request.urlretrieve(url,os.path.dirname(__file__)+"/Data/newton.csv")
    return pandas.read_csv(os.path.dirname(__file__)+"/Data/newton.csv").to_numpy()
def interpolar(puntos):
    f=x+1
    f-=x+1
    for i in range(len(puntos)):
        r=1
        s=1
        for j in range(i):
            r*=x-puntos[j,0]
        for j in range(i):
            s*=puntos[i,0]-puntos[j,0]
        a=(puntos[i,1]-sympy.lambdify([x],f,numpy)(puntos[i,0]))/s
        f+=a*r
    return f
def grafica():
    p=cargar()
    fnc=interpolar(p)
    x0=numpy.linspace(0,6,50)
    y0=sympy.lambdify([x],fnc,numpy)(x0)
    plt.plot(x0,y0,label="interpolación")
    plt.title(sympy.simplify(fnc))
    plt.scatter(p[:,0],p[:,1],color="r",label="Data")
    plt.legend()
    plt.show()
while True:
    a=input("""\nProblema 3.13.5 Interpolación Newton-Gregory\nSeleccione:
1. Interpolar los puntos dados.\n2. salir\n""")
    if a=="1":
        grafica()
    elif a=="2":
        print("adios")
        break
    else:
        print("opción inválida")