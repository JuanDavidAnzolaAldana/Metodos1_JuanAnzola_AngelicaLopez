#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import sympy as sym


# In[2]:


#Definir matrices
l21 = sym.Symbol('l21', real=True)
l31 = sym.Symbol('l31', real=True)
l32 = sym.Symbol('l32', real=True)

u11 = sym.Symbol('u11', real=True)
u12 = sym.Symbol('u12', real=True)
u13 = sym.Symbol('u13', real=True)
u22 = sym.Symbol('u22', real=True)
u23 = sym.Symbol('u23', real=True)
u33 = sym.Symbol('u33', real=True)

A = np.array([[4,-2,1],[20,-7,12],[-8,13,17]])
L = np.array([[1,0,0],[l21,1,0],[l31,l32,1]])
U = np.array([[u11,u12,u13],[0,u22,u23],[0,0,u33]])

#Definir sistema de ecuaciones
LU = np.matmul(L,U)

print(LU[0][0], "=", A[0][0])
print(LU[0][1], "=", A[0][1])
print(LU[0][2], "=", A[0][2])
print(LU[1][0], "=", A[1][0])
print(LU[1][1], "=", A[1][1])
print(LU[1][2], "=", A[1][2])
print(LU[2][0], "=", A[2][0])
print(LU[2][1], "=", A[2][1])
print(LU[2][2], "=", A[2][2])


# In[3]:


U[0][0] = A[0][0]
U[0][1] = A[0][1]
U[0][2] = A[0][2]
L[1][0]= A[1][0]/U[0][0]
U[1][1] = A[1][1] - (L[1][0]*U[0][1])
U[1][2] = A[1][2] - (L[1][0]*U[0][2])
L[2][0] = A[2][0]/U[0][0]
L[2][1] = (A[2][1] -(L[2][0]*U[0][1]))/U[1][1]
U[2][2] = A[2][2] - ((L[2][0]*U[0][2]) + (L[2][1]*U[1][2]))

print(L)
print(U)


# In[4]:


A = np.array([[4.,1.,1.],[1.,3.,2.],[1.,2.,5.]])
A


# In[5]:


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


# In[6]:


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
        vectors[:,i] = v
      
        B = A1 - l*Tensor(v)
        A1 = B
        
    return values,vectors

GetEigValues(A)


# In[7]:


np.linalg.eig(A)


# In[ ]:




