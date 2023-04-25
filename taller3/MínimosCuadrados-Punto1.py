#!/usr/bin/env python
# coding: utf-8

# Parte (a)

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


# In[3]:


b = np.array([2,1,4])
A = np.array([[2.,-1.],[1.,2.],[1.,1.]])
A
b


# In[4]:


def GetFit(A,b,n=2):
    
    n = A.shape[0]
        
    AT = np.dot(A.T,A)
    bT = np.dot(A.T,b)
    
    xsol = np.linalg.solve(AT,bT)
    
    return xsol

n = 2
param = GetFit(A,b,n)
param


# In[5]:


minim = np.linalg.norm(np.dot(A,param) - b)
minim


# In[6]:


x = np.linspace(-5,5)
y1 = 2*x - 2
y2 = 0.5 - (x/2)
y3 = 4 - x

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.scatter(param[0],param[1])


# Parte (b)

# In[7]:


def f(x,y):
    func = np.array([[2*x - y - 2],[x + 2*y - 1],[x + y - 4]])
    rta = np.linalg.norm(func)
    return rta

h = 0.01
x = np.linspace(-5,5,1000)
y = np.linspace(-5,5,1000)

dlist = []
xlist = []
ylist = []
dmin = 10000

for i in range(len(x)):
    for j in range(len(y)):

        d = np.linalg.norm(f(x[i],y[j]))
        xlist.append(x[i])
        ylist.append(y[j])
        dlist.append(d)
        if d <= dmin:
            dmin = d
            xmin = x[i]
            ymin = y[j]


print(dmin)
print(xmin)
print(ymin)


# In[9]:


def f(x, y):
    return np.array([[2*x - y - 2], [x + 2*y - 1], [x + y - 4]])


x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
X, Y = np.meshgrid(x, y)
Z = np.zeros([len(x), len(y)])
for i in range(len(x)):
    for j in range(len(y)):
        Z[i, j] = np.linalg.norm(f(x[i], y[j]))

print(len(Z))

ax = plt.figure(figsize=(6, 6)).add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap='coolwarm')
ax.view_init(azim=60, elev=30)

plt.show()


# In[ ]:




