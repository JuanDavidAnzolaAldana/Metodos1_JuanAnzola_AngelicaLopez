#!/usr/bin/env python
# coding: utf-8

# In[54]:


import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import numpy as np
import sympy as sym
import os.path as path
import os
import urllib.request


# In[55]:


if not path.exists('Data'):
    os.mkdir('Data')
    
filename = 'Data/Parabolico.dat'
url = 'https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Parabolico.csv'
urllib.request.urlretrieve(url, filename)

if not path.exists(filename):
    Path_ = np.loadtxt(filename)
    
else:
    Path_ = filename
    
Data = pd.read_csv(Path_)

X = np.float64(Data.X)
Y = np.float64(Data.Y)
print (X,Y)


# In[56]:


def Lagrange(x,xi,j):
    
    prod = 1.0
    n = len(xi)
    
    for i in range(n):
        if i != j:
            prod *= (x - xi[i])/(xi[j]-xi[i])
            
    return prod

def Interpolate(x,xi,yi):
    
    Sum = 0.
    n = len(xi)
    
    for j in range(n):
        Sum += yi[j]*Lagrange(x,xi,j)
        
    return Sum

x = np.linspace(X[0],X[-1],100)
y = Interpolate(x,X,Y)

plt.scatter(X,Y,marker='o',color='r')
plt.plot(x,y,color='k')


# In[57]:


x = sym.Symbol('x',real = True)
f = Interpolate(x,X,Y)
f = sym.simplify(f)
f


# In[58]:


func = sym.lambdify([x],f,'numpy')

def y_max(f):
    ymax = np.max(f(X))
    return ymax

ymax = y_max(func)
print(ymax)


# In[67]:


dy = Y[-1] - Y[0]
R = 5.6 - 1.4
g = -9.8
v0y = (2*abs(g)*(ymax-Y[0]))**0.5
t = -v0y - ((v0y**2) + 2*g*dy)*0.5
t = t/g
v0x = R/t
v0 = (v0y**2 + v0x**2)**0.5
theta = np.arctan(v0y/v0x)
theta = theta*180/np.pi
print(v0,theta)


# In[ ]:




