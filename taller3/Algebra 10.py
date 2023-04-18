import numpy
matriz=numpy.array([[1,2,-1],
                    [1,0,1],
                    [4,-4,5]])
def Propio(mat,c):
    new=numpy.array([0,0,0])
    new[c]=1
    oldl=1
    newl=9999
    while numpy.abs(oldl-newl)>1e-18:
        old=new
        oldl=newl
        new=mat@old
        newl=new[c]/old[c]
        new=new/numpy.linalg.norm(new)
    return newl,new
def ProductoTensorial(vector,bector):
    T=numpy.zeros([vector.shape[0],bector.shape[0]])
    for i in range(len(vector)):
        for j in range(len(bector)):
            T[i,j]=vector[i]*bector[j]
    return T
def Propios(mat):
    triz=mat.copy()
    valores=numpy.zeros(mat.shape[0])
    vetores=numpy.zeros(mat.shape)
    for i in range(len(mat)):
        l, v=Propio(triz,i)
        valores[i]=l
        vetores[i]=v
        triz=triz-l*ProductoTensorial(v,v)
    return valores,vetores
val,vec=Propios(matriz)
val=val[len(val)-1]
matriz=matriz-(numpy.eye(3)*val)
def norma(vector):
    return numpy.sum(vector**2)**(1/2)
def func(vector):
    return norma(matriz@vector)
def derivada(f,r,h):
    return (f(r+h)-f(r-h))/(2*(norma(h)))
def gradiente(f,r,h):
    grad = numpy.array([0.0, 0.0, 0.0])
    for i in range(len(grad)):
        delta=numpy.zeros(grad.shape)
        delta[i]=h
        grad[i]=derivada(f,r,delta)
    return grad
def descenso(f,r):
    grad=numpy.zeros((3))
    dist=0.5
    while dist>1e-16:
        last=grad
        grad=gradiente(f,r,0.00001)
        grad=grad/norma(grad)
        if numpy.sum(last*grad)<0:
            dist/=2
        r-=dist*grad
    return r/norma(r)
vec=descenso(func,numpy.array([1.0,0.0,0.0]))
print("El valor de estado base es:")
print(val)
print("Su vector propio asociado es:")
print(vec)