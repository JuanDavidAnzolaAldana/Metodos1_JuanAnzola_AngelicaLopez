def iteracion(x,valor):
    return (valor+(x/valor))/2
def algoritmoBabilonico(x):
    valor=x
    print(valor)
    for i in range(10):
        valor=iteracion(x,valor)
        print(valor)
    return valor
x=float(3)
print("La raiz de "+ str(x)+" es "+str(algoritmoBabilonico(x)))
def Transformacion(vector):
    matrix=[[4,2],[1,2]]
    Vect=[]
    for i in matrix:
        num=0
        for j in range(2):
            num+=i[j]*vector[j]
        Vect.append(num)
    return Vect
vector=[1,2]
print("La transformacion de "+str(vector)+" es igual a "+str(Transformacion([1,2])))