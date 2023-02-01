import numpy
import time
import matplotlib.pyplot as plt
class particle:
    def __init__(self,r0:list,v0:list,a0:list,t,m=1,radius=0.3,Id=1):
        self.r=r0
        self.v=v0
        self.a=a0
        self.time=t
        self.radius=radius
        self.t=0
    def evolucion(self,s):
        self.t=s-self.time
        self.time=s
        self.r[0]+=self.v[0]*self.t+(self.a[0]*self.t**2)/2
        self.r[1]+=self.v[1]*self.t+(self.a[1]*self.t**2)/2
        if self.r[0]>10 or self.r[0]<0:
            self.v[0]=-abs(self.v[0])
        if self.r[0]>10:
            self.v[0]=abs(self.v[0])
        if self.r[1]>10 or self.r[0]<0:
            self.v[1]=-abs(self.v[1])  
        if self.r[1]>10:
            self.v[1]=abs(self.v[0])
        self.v[0]+=self.a[0]*self.t
        self.v[1]+=self.a[1]*self.t
times=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1,8,1.9,2.0]
p1=particle([0.0,0.0],[5.0,10.0],[0.0,-1.0],0.0)
for i in times:
    p1.evolucion(i)
    print("tiempo: "+str(i))
    print("posición: "+str(p1.r))
    fig,ax=plt.subplots()
    ax.scatter([p1.r[0]],[p1.r[1]],s=p1.radius*500)
    ax.set(xlim=(0, 8), xticks=numpy.arange(1, 8),
       ylim=(0, 8), yticks=numpy.arange(1, 8))
    plt.show()
    time.sleep(i)
        