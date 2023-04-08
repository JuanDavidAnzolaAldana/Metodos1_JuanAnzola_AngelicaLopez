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
print("El valor de estado base es:")
print(val[len(val)-1])
print("Su vector propio asociado es:")
print(vec[len(val)-1])