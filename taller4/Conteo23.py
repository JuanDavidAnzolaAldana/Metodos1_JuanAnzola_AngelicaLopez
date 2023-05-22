#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# Si asignamos a cada color una variable, x,y y z podemos ver que posibles combinaciones podríamos tener. En el caso de elegir 3 llaves del mismo color y una de otro tenemos x-x-x-y, y-y-y-x, x-x-x-z, z-z-z-x, y-y-y-z, z-z-z-y, que darían un total de 6 combiniaciones. En un segundo caso en el que tengamos 2 llaves de un color y 2 de otro tendríamos x-x-y-y, x-x-z-z, y-y-z-z para un total de 3 combinaciones de colores posibles. En un último caso, si elegimos 2 llaves de un mismo color y 2 de colores diferentes tenemos x-x-y-z, y-y-x-z, z-z-x-y para un total de 3 combianciones. Sumando todos los casos tenemos 12 posibles combinaciones.

# In[2]:



num_distrib = np.math.factorial(3)+ 2*3

num_distrib


# In[ ]:




