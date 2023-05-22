#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


nums = np.array([0,1,2,3,4,5,6,7,8,9,10])
suma = []
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            sumai = nums[i]+ nums[j] + nums[k]
            suma.append(sumai)

count = 0
for l in range(len(suma)):
    if suma[l] == 10:
        count += 1

count


# In[ ]:




