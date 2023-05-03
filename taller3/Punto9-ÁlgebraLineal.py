#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np


# In[12]:


A = np.array([[4.,1.,1.],[1.,3.,2.],[1.,2.,5.]])
A


# In[43]:


def EigValue(A,c=0,itmax=1000,tolerancia=1e-18):
    
    n = A.shape[0]
    v0 = np.zeros(n)
    
    v0[c] = 1.    
    lambda0 = np.inf 
    
    for k in range(itmax):
        
        v1 = np.dot(A,v0)
        lambda1 = v1[c]/v0[c]
        
        v1 = v1/np.linalg.norm(v1)
                    
        if np.abs(lambda0 - lambda1) <= tolerancia:
            break
           
        lambda0 = lambda1
        v0 = v1
                 
    return lambda0,v0

EigValue(A)


# In[47]:


def Tensor(v):
    
    n = v.shape[0]
    T = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            T[i,j] = v[i]*v[j]
    
    return T

def GetEigValues(A):
    
    A1 = A.copy()
    
    values = np.zeros(A1.shape[0])
    vectors = np.zeros_like(A1)
    
    for i in range(A.shape[0]):
        
        l,v = EigValue(A1,i) 
        
        values[i] = l
        vectors[:,i] = v* (-1)**i
      
        B = A1 - l*Tensor(v)
        A1 = B
        
    return values,vectors

GetEigValues(A)


# In[45]:


np.linalg.eig(A)


# In[ ]:




