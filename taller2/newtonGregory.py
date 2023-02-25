import os
import urllib.request
import numpy
import pandas
import sympy
import matplotlib.pyplot as plt
puntos=numpy.zeros((1,2))
def cargar():
    global puntos
    if not os.path.exists(os.path.dirname(__file__)+"/Data"):
        os.mkdir(os.path.dirname(__file__)+"/Data")
    if not os.path.exists(os.path.dirname(__file__)+"/Data/newton.csv"):
        url="https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/InterpolacionNewtonNoequi.csv"
        urllib.request.urlretrieve(url,os.path.dirname(__file__)+"/Data/newton.csv")
    puntos=pandas.read_csv(os.path.dirname(__file__)+"/Data/newton.csv").to_numpy()
def grafica():
    plt.scatter(puntos[:,0],puntos[:,1],color="r",label="Data")
    plt.legend()
    plt.show()
cargar()
grafica()