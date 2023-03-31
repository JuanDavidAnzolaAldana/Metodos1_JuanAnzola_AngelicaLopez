#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import sympy
import matplotlib.pyplot as plt


# Punto 22
# 

# parte (a)

# Para un anillo de radio a, un punto de este identificado con el ángulo f, la posición puede describirse así:
# $$x_0=a cos(f) \\
# y_0=a sin(f) \\
# z_0=0$$
# La distancia a un punto en las coordenadas (x,y,z) sería:
# $$x_1=a cos(f)-x \\
# y_1=a sin(f)-y \\
# z_1=-z$$
# El valor absoluto de la distasncia es:
# $$||r||=\sqrt{(a cos(f)-x)^2+(a sin(f)-y)^2+z^2}$$
# La magnitud del campo eléctrico se define como:
# $$||E||=\frac{1}{4\pi\epsilon}\frac{Q}{||r||^2}=\frac{1}{4\pi\epsilon}\frac{Q}{(a cos(f)-x)^2+(a sin(f)-y)^2+z^2}$$
# El componente en x del campo eléctrico es:
# $$Ex=||E||\frac{x_1}{||r||}=||E||\frac{a cos(f)-x}{\sqrt{(a cos(f)-x)^2+(a sin(f)-y)^2+z^2}}$$
# $$ Ex= \frac{1}{4\pi\epsilon}\frac{Q}{||r||^2}=\frac{1}{4\pi\epsilon}\frac{Q}{(a cos(f)-x)^2+(a sin(f)-y)^2+z^2}*\frac{a cos(f)-x}{\sqrt{(a cos(f)-x)^2+(a sin(f)-y)^2+z^2}}$$
# $$ Ex=\frac{1}{4\pi\epsilon}\frac{Q(a cos(f)-x)}{((a cos(f)-x)^2+(a sin(f)-y)^2+z^2)^\frac{3}{2}}$$
# $$ Ex=\frac{1}{4\pi\epsilon}\frac{Q(a cos(f)-x)}{((a^2cos^2(f) - 2axcos(f)+ x^2)+(a^2sin^2(f) - 2aysin(f)+ y^2)+z^2)^\frac{3}{2}}$$
# $$ Ex=\frac{1}{4\pi\epsilon}\frac{Q(a cos(f)-x)}{(a^2-2axcos(f)+ x^2-2aysin(f)+ y^2+z^2)^\frac{3}{2}}$$
# Para las otras coordenadas el proceso es analogo
# Solo hace falta integrarpara obtener la fórmula dada.

# parte (b)

# In[12]:


x=sympy.Symbol("x",real=True)
y=sympy.Symbol("y",real=True)
z=sympy.Symbol("z",real=True)
a=sympy.Symbol("a",real=True)
f=sympy.Symbol("f",real=True)
integralx=(x-a*sympy.cos(f))/((x**2+y**2+z**2+a**2-2*a*x*sympy.cos(f)-2*a*y*sympy.sin(f))**(3/2))
integraly=(y-a*sympy.sin(f))/((x**2+y**2+z**2+a**2-2*a*x*sympy.cos(f)-2*a*y*sympy.sin(f))**(3/2))
integralz=(z)/((x**2+y**2+z**2+a**2-2*a*x*sympy.cos(f)-2*a*y*sympy.sin(f))**(3/2))
def campox(px,py,pz):
    func=sympy.lambdify([x,y,z,a,f],integralx)
    puntos, pesos=numpy.polynomial.legendre.leggauss(20)
    integral=numpy.sum(pesos*func(px,py,pz,0.5,(puntos+1.0)*numpy.pi))/2
    return integral
def campoy(px,py,pz):
    func=sympy.lambdify([x,y,z,a,f],integraly)
    puntos, pesos=numpy.polynomial.legendre.leggauss(20)
    integral=numpy.sum(pesos*func(px,py,pz,0.5,(puntos+1.0)*numpy.pi))/2
    return integral
def campoz(px,py,pz):
    func=sympy.lambdify([x,y,z,a,f],integralz)
    puntos, pesos=numpy.polynomial.legendre.leggauss(20)
    integral=numpy.sum(pesos*func(px,py,pz,0.5,(puntos+1.0)*numpy.pi))/2
    return integral
def campo(px,py,pz):
    return numpy.array([campox(px,py,pz),campoy(px,py,pz),campoz(px,py,pz)])


# parte (c)

# In[11]:


print(campo(0.6,0.6,1))


# parte (d)

# In[16]:


dx=numpy.linspace(-0.6,0.6,6)
dy=numpy.linspace(-0.6,0.6,6)
dz=numpy.linspace(-0.6,0.6,6)
X,Y,Z = numpy.meshgrid(dx,dy,dz)


# parte (e)

# In[18]:


Ex = numpy.zeros((6,6,6))
Ey = numpy.zeros((6,6,6))
Ez = numpy.zeros((6,6,6))


# parte (f)

# In[20]:


fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111,projection='3d')
for i in range(6):
    for j in range(6):
        for k in range(6):
            Ex[i,j,k]=campox(dx[i],dy[j],dz[k])
            Ey[i,j,k]=campoy(dx[i],dy[j],dz[k])
            Ez[i,j,k]=campoz(dx[i],dy[j],dz[k])
            ax.quiver(dx[i],dy[j],dz[k],Ex[i,j,k],Ey[i,j,k],Ez[i,j,k])
ax.view_init()


# In[21]:


print(Ex[:,:,5])
print(Ey[:,:,5])


# Punto 6

# In[33]:


num=100000
x=numpy.zeros([num])
y=numpy.zeros([num])
z=numpy.zeros([num])
test=numpy.ones([num])
for i in range(num):
    x[i]=numpy.random.uniform(-1,1)
    y[i]=numpy.random.uniform(-1,1)
    z[i]=numpy.random.uniform(-1,1)
    if x[i]**2+y[i]**2+z[i]**2>1:
        x[i]=0
        y[i]=0
        z[i]=0
        test[i]=0
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111,projection='3d')
ax.scatter(x,y,z)
plt.show()
integralxx=numpy.sum((y**2+z**2)*test)/numpy.sum(test)
print("Ixx: ",integralxx)
integralyy=numpy.sum((x**2+z**2)*test)/numpy.sum(test)
print("Iyy: ",integralxx)
integralzz=numpy.sum((y**2+z**2)*test)/numpy.sum(test)
print("Izz: ",integralxx)


# In[34]:


integralxy=-numpy.sum((y*x)*test)/numpy.sum(test)
print("Ixy: ",integralxx)


# La esfera es perfectamente simétrica porque su momento de inercia es exactamente el mismo en todos los ejes.

# In[ ]:




