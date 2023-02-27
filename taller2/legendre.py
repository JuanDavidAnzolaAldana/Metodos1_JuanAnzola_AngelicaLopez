import sympy
import numpy
x=sympy.Symbol("x",real=True)
def legendre(n):
    f=(x**2-1)**n
    for i in range(n):
        f=sympy.diff(f,x)
    return sympy.simplify(f/(2**n*numpy.math.factorial(n)))
print(legendre(0))
print(legendre(1))
print(legendre(2))
print(legendre(3))
print(legendre(4))
print(legendre(5))
print(legendre(6))
print(legendre(7))
print(legendre(8))