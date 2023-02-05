import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import tqdm
import time

class bounding_box:
    def __init__(self, size:tuple, pos:tuple):
        self.size=size
        self.pos=pos
    def get_limits_x(self)->tuple:
        return (self.pos[0],self.pos[0]+self.size[0])
    def get_limits_y(self)->tuple:
        return (self.pos[1],self.pos[1]+self.size[1])
class particle:
    def __init__(self, pos:numpy.ndarray, vel:numpy.ndarray, mass:float, radius:float):
        self.pos=pos
        self.vel=vel
        self.mass=mass
        self.r=radius
        self.t=0
    def get_status(self)->numpy.ndarray:
        state=numpy.zeros((2,2))
        state[0]=self.pos
        state[1]=self.vel
        return state
    def update_physics(self,dt:float)->None:
        self.pos+=self.vel*dt
def testlib()->None:
    print(type(numpy.zeros((2,2))))
    for i in tqdm.tqdm(range(10)):
        time.sleep(0.2)
    fig=plt.figure(figsize=(5,5))
    ax=fig.add_subplot()
    ax.plot(numpy.arange(10),numpy.arange(10))
    plt.show()
def simulate(particles:list,bounds:bounding_box,maxtime:float,deltatime:float)->list:
    timeline=numpy.arange(0,maxtime,deltatime)
    info=[]
    for i in tqdm.tqdm(particles, desc="preparando estructuras de datos"):
        info.append(numpy.zeros((len(timeline),2,2)))
    for i in tqdm.tqdm(range(len(timeline)),desc="procesando"):
        for j in range(len(particles)):
            info[j][i]=particles[j].get_status()
            particles[j].update_physics(deltatime)
    return (info,timeline)
def simulation(tf:float,dt:float)->None:
    box=bounding_box((40,40), (-20,-20))
    particles=[particle(numpy.array([-15.0,1.0]), numpy.array([10.0,0.0]), 1.0, 2.0),
               particle(numpy.array([0.0,-1.5]), numpy.array([0.0,0.0]), 1.0, 2.0)]
    info,tl=simulate(particles,box,tf,dt)
    fig=plt.figure(figsize=(5,5))
    ax=fig.add_subplot()
    def start():
        ax.set(xlim=box.get_limits_x(),ylim=box.get_limits_y())
    def update(i):
        ax.clear()
        start()
        ax.set_title(r'$ t=%.2f \ s$' %(tl[i]))
        for j in range(len(info)):
            st=info[j][i]
            ax.add_patch(plt.Circle((st[0,0],st[0,1]),particles[j].r, fill=True, color='k'))
            ax.arrow(st[0,0],st[0,1],st[1,0],st[1,1],color='r',head_width=0.2,length_includes_head=True)
    start()
    Animation = anim.FuncAnimation(fig,update,frames=len(tl),init_func=start)
    plt.show()
#testlib()
simulation(5,0.01)
