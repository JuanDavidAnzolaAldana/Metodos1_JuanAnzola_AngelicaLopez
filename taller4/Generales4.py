#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def P(p):
    P = 1
    for i in range(p):
        P0 = (365-i)/365
        P *= P0
    
    return P

#Para 365 personas
P_365 =P(365)
P_365


# In[3]:


#Para 80...0 personas
Ps = []
for j in range(1,81):
    a = P(j)
    Ps.append(a)

Ps


# In[4]:


#Gráfica
x = np.arange(1,81)
plt.scatter(x,Ps)


# In[ ]:




