#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# Parte a)

# In[4]:


def f(x,y):
    p = y #número de protones en la muestra
    e = x #número de electrones en la muestra
    if p + e <= 4:
        n = 4-x-y #número de neutrones en la muestra
    else:
        n = 0

    Ce = np.math.factorial(3)/np.math.factorial(e)
    Cp = np.math.factorial(2)/np.math.factorial(p)
    Cn = np.math.factorial(3)/np.math.factorial(n)
    C = np.math.factorial(8)/np.math.factorial(4)
    f = Ce*Cp*Cn/C
  
    return f


# In[5]:


F = np.zeros((3,4))
for p in range(3):
    for e in range(4):
        F[p][e] = f(e,p)
F


# Parte b)

# In[6]:


N = np.sum(F)
g = np.sum(F/N, axis =0)
h = np.sum(F/N,axis = 1)
print(g)
print(h)


# Parte c) y d)

# In[7]:


xs = np.array([0,1,2,3])
Ex = np.sum(xs*g)
ys = np.array([0,1,2])
Ey = np.sum(ys*h)

print(Ex)
print(Ey)


# Parte e) y f)

# In[8]:


Exy = Ex + Ey
covxy = Exy - (Ex*Ey)
covxy


# In[9]:


covxy = np.sum(xs - Ex)* np.sum(ys - Ey)
covxy


# Parte g)

# In[10]:


fs = np.sum(g)*np.sum(h)
print(fs)
print(np.sum(F))


# In[11]:


fs = g[0]*h[0]
Fs = F[0][0]
print(fs)
print(Fs)


# Las variables x e y no son independientes puesto que el producto de las distribuciones marginales es diferente a su distribución conjunta.

# In[ ]:




