#!/usr/bin/env python
# coding: utf-8

# In[30]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from scipy import integrate
from tqdm import tqdm


# In[36]:


def f(x,y,R):
    return ((R**2 - (x**2)+(y**2))**0.5)

def CreateGrilla(N,R1= -1,R2 = 1):
    R = 1
    Points = np.zeros((N+1,2))
        
    for i in tqdm(range(N + 1)):
            
        r = 2*R/N
        x = np.random.uniform(-1,1)
        y = np.random.uniform(-1,1)   
        
        Points[i] = [x,y]
            
    return Points

Grilla = CreateGrilla(500)

R = 1
X = np.linspace(-R, R, 100)
Y = np.linspace(-R, R, 100)
X, Y = np.meshgrid(X, Y)


for i, point in enumerate(Grilla):
    if (((f(point[0], point[1], R))**2 + point[0]**2 + point[1]**2)**0.5) <= R:
        Z = f(X, Y, R)
    else:
        Z = 0
        


# In[37]:


fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111,projection='3d')
ax.scatter(Grilla[:,0],Grilla[:,1])
ax.scatter(Grilla[:, 0], Grilla[:, 1], np.sqrt(R**2 - Grilla[:, 0]**2 - Grilla[:, 1]**2), s=1)
ax.scatter(Grilla[:, 0], Grilla[:, 1], -np.sqrt(R**2 - Grilla[:, 0]**2 - Grilla[:, 1]**2), s=1)
plt.show()


# In[39]:



R = 1
r1 = -1
r2 = 1
N = 100
Sample = np.zeros((N,N))
sumSample = 0
for i in range(N):
    for j in range(N):
    
        ri = np.random.uniform(r1,r2)
        Sample[i][j] = f(ri,ri,R)
        if Sample[i][j] > 0:
            sumSample += Sample


I = np.average(sumSample)
I *= (2*R/N)**2

print(I)


# In[ ]:




