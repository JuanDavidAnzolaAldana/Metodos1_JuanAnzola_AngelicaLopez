#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# Parte a)

# In[2]:


def f(m_ok,m_d):
    Cm_ok = np.math.factorial(7)/(np.math.factorial(7-m_ok)*np.math.factorial(m_ok))
    Cm_d = np.math.factorial(3)/(np.math.factorial(3-m_d)*np.math.factorial(m_d))
    C = np.math.factorial(10)/(np.math.factorial(10-(m_ok+m_d))*np.math.factorial(m_ok+m_d))
    f = Cm_ok*Cm_d/C
    return f

print(f(2,0))
print(f(1,1))
print(f(0,2))


# Parte b)

# In[3]:


E = f(2,0)*0+f(1,1)*1+f(0,2)*2
E

