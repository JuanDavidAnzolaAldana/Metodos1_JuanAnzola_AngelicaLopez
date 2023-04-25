#!/usr/bin/env python
# coding: utf-8

# In[63]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[64]:


df = pd.read_csv("https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Sigmoid.csv")

data = df.to_numpy()

x = data[:,0]
y = data[:,1]


# In[74]:


#modelo de ajuste
def M(x,theta):

    return theta[0]/(theta[1] + np.exp(-theta[2]*x))

#función de costo
def X(x,y,theta,N):

    value = 0.

    for i in range(N):
        value += (y[i] - M(x[i],theta))**2

    return value

def grad_X(x,y,theta,N=10000):

    grad = np.zeros(3)

    da, db, dc = 0.,0.,0.
    for n in range(N):

        da += -2*((y[n] - M(x[n],theta))*(1/(theta[1] + np.exp(-theta[2]*x[n]))))
        db += -2*((y[n] - M(x[n],theta))*(-1*theta[0]/((theta[1] + np.exp(-theta[2]*x[n]))**2)))
        dc += -2*((y[n] - M(x[n],theta))*(theta[0]*np.exp(-theta[2]*x[n])*x[n]/((theta[1] + np.exp(-theta[2]*x[n]))**2)))

    grad[0]= da
    grad[1]= db
    grad[2] = dc

    return grad

N = len(x)
theta= np.array([0,0,0])
e = 0.01
num_e = 10000
gamma = 5e-4
values = np.zeros((num_e,3))

for i in range(num_e):
    g = grad_X(x,y,theta,N)
    theta =theta - gamma*g/(np.sum(g**2)**(1/2))
    values[i] = theta
    
param = values[-1]
print(param)


# In[75]:


plt.plot(values)
plt.show()


# In[76]:


plt.scatter(x,y)

x0 = np.linspace(-10,10,100)
plt.plot(x0,M(x0,param),color="red")
plt.show()


# In[ ]:




