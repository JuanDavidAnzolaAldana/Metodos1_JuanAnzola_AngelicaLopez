import sympy
x=sympy.Symbol("x",real=True)
y=sympy.Symbol("y",real=True)
f=2*(x+2*y)/3
print("La función es:",f)
#¿Es una función de probabilidad?
total=sympy.integrate(sympy.integrate(f,(x,0,1)),(y,0,1))
print("Si la integral de la función es 1, es una función de probabilidad:")
print("La integral de la función es",total)
#distribuciones marginales
g=sympy.integrate(f,(y,0,1))
h=sympy.integrate(f,(x,0,1))
print("La función de probabilidad marginal g(x) es:",g)
print("La función de probabilidad marginal h(y) es:",h)
#Valor esperado
Ex=sympy.integrate(x*g,(x,0,1))
Ey=sympy.integrate(y*h,(y,0,1))
print("El valor esperado E(x) es:",Ex)
print("El valor esperado E(y) es:",Ey)
#Covarianza
Exy=sympy.integrate(sympy.integrate(x*y*f,(x,0,1)),(y,0,1))
print("La covarianza calculada por valores esperados es:",Exy-Ex*Ey)
sigma=sympy.integrate(sympy.integrate((x-Ex)*(y-Ey)*f,(x,0,1)),(y,0,1))
print("La covarianza calculada segun la definición es:",sigma)
print("Ya que la covarianza no es 0, x & y son dependientes")