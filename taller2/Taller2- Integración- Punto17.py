#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import sympy as sym


# In[21]:


x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
y=(x**3/(sym.exp(x) - 1))
y


# In[23]:


n = 3
def GetLaguerre(n ,x,y):
    return sym.exp(x)/sym.factorial(n)*sym.diff( y,x,n )
    
Laguerre = []
DLaguerre = []

for i in range(n+2):
    
    Poly = GetLaguerre(i,x,sym.exp(-x)*(x**i))
    Laguerre.append(Poly)
    DLaguerre.append( sym.diff(Poly,x,1) )



_x = np.linspace(0,20,100)

for i, p in enumerate(Laguerre):
    pn = sym.lambdify([x],p,'numpy')
    print(p)
    if p==1:
        plt.plot(_x,np.ones(_x.size),label=f'L_{i}(x)')
    else:
        plt.plot(_x,pn(_x),label=f'L_{i}(x)')


# In[49]:


xn = np.linspace(1,30,100)
def GetNewtonRaphson(f,df,xn,itmax=10000,precision=1e-5):
    
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

def GetRoots(f,df,x,tolerancia=8):
    
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


def GetWeights(Roots,DLegendre):
    
    n = len(Roots)
    weights = np.zeros(n)
    for i in range(n):
        d_poly = sym.lambdify([x], DLegendre[n+1], 'numpy')
        if d_poly(Roots[i]) != 0:
            weights[i] = np.float64(Roots[i] / ((n + 1) ** 2 * d_poly(Roots[i]) ** 2))
    return weights


Roots=GetAllRoots(n,xn,Laguerre,DLaguerre)
print(Roots)
W = GetWeights(Roots,Laguerre)

print(W)


# In[50]:


x1 = sym.Symbol('x',real=True)
y1 = sym.Symbol('y',real=True)
y1 = x**3/(sym.exp(x) - 1)

def gauss_laguerre_integrate(y,x,n,xn):
    
    Laguerre = []
    DLaguerre = []
    
    for i in range(n+2):
        Poly = GetLaguerre(i, x, sym.exp(-x)*(x**i))
        Laguerre.append(Poly)
        DLaguerre.append(sym.diff(Poly, x, 1))
    Roots = GetAllRoots(n,xn,Laguerre,DLaguerre)
    Roots=Roots[np.logical_not(np.isnan(Roots))]
    W = GetWeights(Roots,Laguerre)
    poly = sym.lambdify([x],y,'numpy')
    
    return np.sum(W*poly(Roots))

Igl = gauss_laguerre_integrate(y1*sym.exp(x1),x1,3,xn)
Igl


# In[51]:


I = np.pi**4/15
I


# In[52]:


def error(n):
    
    I = np.pi**4/15
    Igl = gauss_laguerre_integrate(y*sym.exp(x),x,n,xn)
    Error = Igl/I
    
    return Error

E = []
ns = [2,3,4,5,6,7,8,9,10]
for i in (ns):
    E.append(error(i))

plt.scatter(ns,E, label=f'error')
plt.show()


# In[ ]:




