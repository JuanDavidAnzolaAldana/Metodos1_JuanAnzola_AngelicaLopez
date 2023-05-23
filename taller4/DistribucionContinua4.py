#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy as sc
import scipy.integrate as integrate
import numpy as np


# In[2]:


def E(x):
    E = np.exp(-x/3)
    return E

value, error = integrate.quad(E, 0, np.inf)
value


# In[ ]:




