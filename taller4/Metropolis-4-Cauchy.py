#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import scipy.stats as stats

def Prior(x):
    return 1/(np.pi*(1 + x**2))

def Likelihood(x):
    return np.prod(1/(np.pi*(1 + x**2)))

def Posterior(x):
    return Likelihood(x) * Prior(x)

def Metropolis(x0, posterior_func, n_steps=int(1e4), delta=0.4):
    x = np.zeros(n_steps)
    x[0] = x0
    
    for i in tqdm(range(1, n_steps)):
        x_proposal = x[i-1] + delta * np.random.randn()
        
        p0 = posterior_func(x[i-1])
        p1 = posterior_func(x_proposal)
        
        alpha = min(1, p1 / p0)
        u = np.random.uniform(0,1)
        
        if u < alpha:
            x[i] = x_proposal
        else:
            x[i] = x[i-1]
    
    return x


np.random.seed(0)

x0 = 0 
samples = Metropolis(x0, Posterior, n_steps=1000)

plt.hist(samples, bins=50, density=True)
x = np.linspace(-10, 10, 500)
plt.plot(x, Prior(x), 'r')
plt.show()


# In[ ]:




