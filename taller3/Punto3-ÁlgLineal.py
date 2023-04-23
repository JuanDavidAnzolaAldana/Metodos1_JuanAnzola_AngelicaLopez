#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


A = np.array([[1,0,0],[5,1,0],[-2,3,1]])
B = np.array([[4,-2,1],[0,3,7],[0,0,2]])
A,B


# In[4]:


def MultAB(A,B):
    nc = len(A[0])
    nf = len(A)

    mc = len(B[0])
    mf = len(B)

    B = B.T
    C = np.zeros((nf,mc))

    if mf == nc:
        for i in range(0,nc):
            for j in range (0,mf):
                C[j][i] = np.dot(A[j],B[i])

    return C


# In[5]:


print(MultAB(A,B))


# In[ ]:




