import numpy
import matplotlib.pyplot as plt
h=0.2
x0=0
x=[]
y=[]
y2=[]
y3=[]
y4=[]
for i in range(int(6/h)):
    x.append(x0+h*i)
    y.append(numpy.sin(x0+h*i))
for i in range(1,len(y)):
    y2.append((y[i]-y[i-1])/h)
for i in range(0,len(y)-1):
    y3.append((y[i+1]-y[i])/h)
for i in range(1,len(y)-1):
    y4.append((y[i+1]-y[i-1])/(2*h))
plt.scatter(x,y,label="f(x)")
x2=x.copy()
x2.pop(0)
x3=x.copy()
x3.pop(-1)
x4=x3.copy()
x4.pop(0)
plt.scatter(x2,y2,label="izquierda")
plt.scatter(x3,y3,label="derecha")
plt.scatter(x4,y4,label="central")
plt.legend()
plt.show()