#Problema 2.03 Sucesión de fivonacci
import numpy
import matplotlib.pyplot as plt
#Requisito 1
def fivonnacci(x:int)->list:
    fiv=[0,1]
    for i in range(2,x+1):
        fiv.append(fiv[-1]+fiv[-2])
    return fiv
#Requisito 2
def succesion_plot():
    plt.plot(numpy.arange(21),fivonnacci(20),label="Serie Fivonnaci",color="black")
    plt.legend()
    plt.show()
#Requisito 3
def gold_plot():
    fiv=fivonnacci(20)
    gold=[]
    for i in range(2,len(fiv)):
        gold.append(fiv[i]/fiv[i-1])
    plt.plot(numpy.arange(len(gold)),gold,label="Estimación usando la serie",color="b")
    plt.axhline(y=(1+5**(1/2))/2,color="r",ls="--",label="Número aureo")
    plt.legend()
    plt.show()

while True:
    a=input("""\nProblema 2.03 Sucesión de fivonnaci\nSeleccione:
1. Encontrar los primeros 20 términos de la sucesión.\n2. Graficar la sucesión.
3. Calcular el número aureo y comparar con el valor exacto.\n4. salir\n""")
    if a=="1":
        print("los 20 primeros términos son ",fivonnacci(20))
    elif a=="2":
        succesion_plot()
    elif a=="3":
        gold_plot()
    elif a=="4":
        print("adios")
        break
    else:
        print("opción inválida")