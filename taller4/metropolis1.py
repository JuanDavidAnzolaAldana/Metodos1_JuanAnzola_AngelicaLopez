import numpy
import emcee
import tqdm
import corner
import matplotlib.pyplot as plt
def prior(p):
    if type(p) is numpy.ndarray:
        q=numpy.zeros(len(p))
        for j in range(len(p)):
            if 0<=p[j] and p[j]<=1:
                q[j]=1
            else:
                q[j]=0
        return q
    else:
        if 0<=p and p<=1:
            return 1
        else:
            return 0
    
def likelihood(p):
    return (p**7)*((1-p)**3)
def posterior(p):
    return likelihood(p)*prior(p)
def Metropolis(Post,delta= 0.4):
    x=numpy.zeros((10000))
    x[0]=0.5
    for i in tqdm.trange(1,10000):
        P0=Post(x[i-1])
        xf=x[i-1]+delta*2*(numpy.random.rand()-0.5)
        P1=Post(xf)
        alpha=numpy.minimum( 1, P1/P0 )
        g=numpy.random.rand()
        if alpha > g:
            x[i]=xf
        else:
            x[i]=x[i-1]     
    return x
cadena=Metropolis(posterior)
plt.hist(cadena,bins=20,density=True,label="Metrópolis")
x0=numpy.linspace(0,1,100)
y0=posterior(x0)
plt.plot(x0,y0*1320,c="r",label="posterior")
plt.title("El algoritmo de metrópolis encaja con la función de probabilidad posterior")
plt.legend()
plt.show()
trouts=numpy.percentile(cadena, 50)
corner.corner(cadena,truths=[trouts],labels="Probabilidad",show_titles=True)
plt.show()
print("Puesto que el modelo con probabilidad 0.5 está fuera del margen de error del modelo más probable, se puede decir que la moneda está trucada. Sin embargo, aún es relativamente probable que la moneda no esté trucada ya que modelo con probabilidad 0.5 está demasiado cerca del margen de error del modelo más probable.")