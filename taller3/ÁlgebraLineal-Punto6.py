#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


A = np.array([[3,-1,-1],[-1.,3.,1.],[2.,1.,4.]])
b = np.array([1.,3.,7.])


# In[3]:


def GausSeidel(A, b, x0, w, itmax=10000, tolerancia=1e-9):
    x = list(x0)
    it = 0
    while it < itmax:
        for i in range(A.shape[0]):
            sum_ = 0.
            sum_2 = 0.
            for j in range(i):
                sum_ += A[i, j] * x[j]
            for j in range(i+1, A.shape[1]):
                sum_2 += A[i, j] * x[j]
            x[i] = (1 - w)*x[i] + (w / A[i, i]) * (b[i] - sum_ - sum_2)
        residuo = np.linalg.norm(np.dot(A, x) - b)
        it += 1

        if np.allclose(residuo, tolerancia, atol=tolerancia):
            break
        for j in range(len(x)):
            if np.isinf(x[j]) or np.isnan(x[j]):
                return x0, w, itmax
    return x, w, it

itmin = 10000
bestw = 0
x = np.array([1.5, 1.2, 1.3])
solucion = np.array([1.1, 1.2, 1.3])


for w in np.linspace(1, 2, 2):
    x_solucion, w, it = GausSeidel(A, b, x, w)
    if it < itmin:
        itmin = it
        bestw = w
        solucion = x_solucion


print(solucion)
print(bestw)
print(itmin)


# In[ ]:




