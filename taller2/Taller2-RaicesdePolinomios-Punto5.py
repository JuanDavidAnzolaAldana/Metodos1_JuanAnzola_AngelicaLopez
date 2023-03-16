#!/usr/bin/env python
# coding: utf-8

# In[64]:


import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import numpy as np
import sympy as sym


# In[65]:


x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
n = 20
y = sym.exp(-x)*x**n

def GetLaguerre(n ,x,y):
    return sym.exp(x)/sym.factorial(n)*sym.diff( y,x,n )
    
Laguerre = []
DLaguerre = []
for i in range(n+1):
    Poly = GetLaguerre(i, x, y)
    Laguerre.append(Poly)
    DLaguerre.append(sym.diff(Poly, x, 1))




xn = np.linspace(0,20,100)

for i, p in enumerate(Laguerre):
    pn = sym.lambdify([x],p,'numpy')
    plt.plot(xn,pn(xn),label=f'L_{i}(x)')


# In[66]:


for i in range(20):
    print(Laguerre[i])
    print("\n")


# In[67]:



for i, p in enumerate(Laguerre):
    pn = sym.lambdify([x],p,'numpy')
    plt.plot(xn,pn(xn),label=f'L_{i}(x)')
        


# In[68]:


def GetNewtonRaphson(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn

def GetRoots(f,df,x,tolerancia=3):
    
    Roots = np.array([])
    
    for i in x:
        root = GetNewtonRaphson(f,df,i)
        
        if root != False:
            
            croot = np.round(root, tolerancia)
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
        
    return Roots


def GetAllRoots(n,xn,Laguerre,DLaguerre):
    poly = sym.lambdify([x],Laguerre[n],'numpy')
    Dpoly = sym.lambdify([x],DLaguerre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)
    return Roots

xn = np.linspace(0,100,200)
Roots = GetAllRoots(19,xn,Laguerre,DLaguerre)
print(Roots)


# In[ ]:




