import numpy
import matplotlib.pyplot as plt
from tqdm import tqdm
puntos=None
pesos=None
def funcion(x,dt,T):
    return numpy.tanh(((((x**2)+(dt**2))**(1/2))*300)/(2*T))/(((x**2)+(dt**2))**(1/2))
def crearFuncion():
    x0=numpy.linspace(-1.5,1.5,200)
    for i in range(1,22,2):
        plt.plot(x0,funcion(x0,0,i),label="T="+str(i))
    plt.legend()
    plt.title("Funciones a integrar para varios T")
    plt.show()
def PuntosYPesos():
    p,w=numpy.polynomial.legendre.leggauss(50)
    plt.quiver(p,numpy.zeros(p.shape),0,w,color="b")
    plt.axhline(0,color="r")
    plt.xlabel("puntos")
    plt.ylabel("pesos")
    plt.show()
    return p,w
def TemperaturaCritica():
    x=numpy.arange(1,20,0.0001)
    y=numpy.arange(1,20,0.0001)
    j=0
    best=1000000000000000000
    tc=-1
    print(1/0.3)
    for i in tqdm(numpy.nditer(x), desc='Calculating integral', unit=' Steps'):
        integral=numpy.sum(pesos*funcion(puntos,0,i))/2
        y[j]=integral
        j+=1
        if numpy.abs((integral)-(1/0.3))<best:
            best=numpy.abs(integral-(1/0.3))
            tc=i
    plt.axhline(1/0.3,color="r")
    plt.plot(x,y)
    plt.scatter([tc],(1/0.3),color="k")
    plt.show()
    return tc
while True:
    a=input("""\nProblema 3.14.19 Spuerconductividad\nSeleccione:
1. Crear la función a integrar.\n2. Cargar los puuntos y pesos de la cuadratura e gauss.
3. Calcular la temperatura crítica.\n4. Salir.\n""")
    if a=="1":
        crearFuncion()
    elif a=="2":
        puntos, pesos=PuntosYPesos()
    elif a=="3":
        print("Calculando temperatura crítica ...")
        temp=TemperaturaCritica()
        print("La temperatura crítica es "+str(temp))
    elif a=="4":
        print("adios")
        break
    else:
        print("opción inválida")