import numpy
import sympy
#Punto a
print("Punto a:")
def tangente4(func,point,delta):
    return(-func(point+2*delta)+8*func(point+delta)-8*func(point-delta)+func(point-2*delta))/(12*numpy.sum(delta**2)**(1/2))
def Jacobiano4(func,point,delta):
    matriz=numpy.zeros([3,3])
    deltax=numpy.array([delta,0.0,0.0])
    matriz[0]=tangente4(func,point,deltax)
    deltay=numpy.array([0.0,delta,0.0])
    matriz[1]=tangente4(func,point,deltay)
    deltaz=numpy.array([0.0,0.0,delta])
    matriz[2]=tangente4(func,point,deltaz)
    return numpy.linalg.det(matriz)
print("La función ha sido creada y está en el código")
#Punto b
print("Punto b:")
x=sympy.Symbol("x",real=True)
y=sympy.Symbol("y",real=True)
z=sympy.Symbol("z",real=True)
fx=6*x-2*sympy.cos(y*z)-1
fy=9*y+sympy.sqrt(x**2+sympy.sin(z)+1.06)+0.9
fz=60*z+sympy.exp(-x*y)+10*sympy.pi-3
def funcionVectorial(point):
    x0=point[0]
    y0=point[1]
    z0=point[2]
    return numpy.array([sympy.lambdify([x,y,z],fx)(x0,y0,z0),sympy.lambdify([x,y,z],fy)(x0,y0,z0),sympy.lambdify([x,y,z],fz)(x0,y0,z0)])
print("El jacobiano de orden h4 de la función dada en el punto (0.5,0.5,0.5) con error de 0.01 es:")
print(Jacobiano4(funcionVectorial,numpy.array([0.5,0.5,0.5]),0.01))
#Punto c
print("Punto c:")
def tangente2(func,point,delta):
    return(func(point+delta)-func(point-delta))/(2*numpy.sum(delta**2)**(1/2))
def Jacobiano2(func,point,delta):
    matriz=numpy.zeros([3,3])
    deltax=numpy.array([delta,0.0,0.0])
    matriz[0]=tangente2(func,point,deltax)
    deltay=numpy.array([0.0,delta,0.0])
    matriz[1]=tangente2(func,point,deltay)
    deltaz=numpy.array([0.0,0.0,delta])
    matriz[2]=tangente2(func,point,deltaz)
    return numpy.linalg.det(matriz)
print("El jacobiano de orden h2 de la función dada en el punto (0.5,0.5,0.5) con h de 0.01 es:")
print(Jacobiano2(funcionVectorial,numpy.array([0.5,0.5,0.5]),0.01))
print("Para igualar en error del jacobiano de orden h4 con h de 0.1, el hacobiano de orden h2 debe tener h de 0.0001")
print("El jacobiano de orden h2 de la función dada en el punto (0.5,0.5,0.5) con h de 0.0001 es:")
print(Jacobiano2(funcionVectorial,numpy.array([0.5,0.5,0.5]),0.0001))
