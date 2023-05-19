import numpy
import emcee
import matplotlib.pyplot as plt
def prior(p):
    if type(p) is numpy.ndarray:
        q=numpy.zeros(len(p))
        for i in range(len(p)):
            if 0<=p[i] and p[i]<=1:
                q[i]=1
            else:
                q[i]=0
        return q
    else:
        if 0<=p[i] and p[i]<=1:
            return 1
        else:
            return 0
    
def likelihood(p,x):
    return (p**x)*((1-p)**(1-x))
def posterior(p,dat):
    producto=1
    for i in numpy.nditer(dat):
        producto*=likelihood(p,i)
    return producto*prior(p)
def Metropolis(dat,func):
    pass
data=numpy.ones(10)
data[0]=0.0
data[1]=0.0
data[2]=0.0
x0=numpy.linspace(-1,2,100)
y0=posterior(x0, data)
plt.plot(x0,y0)
plt.show()
Metropolis(data, posterior)