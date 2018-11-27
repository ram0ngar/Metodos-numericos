#Biseccion
import math
import numpy as np
import matplotlib.pyplot as plt
def fun(y):
    return 1-((20**2)/(9.8*(3*y+((y**2)/2))**3))*(3+y)

#Elegir valores iniciales x0 y x1
#Donde haya un cambio de signo
xarray=np.linspace(10,25,100)
yarray=np.zeros(100)

for i in range(100):
    yarray[i]=fun(xarray[i])

plt.plot(xarray,yarray)
plt.grid()
x0=0.5
x1=2.5
iteracion=0
for i in range(10):
    f0=fun(x0)
    f1=fun(x1)
    if f0*f1>0:
        print("No hay raiz en este rango")
        break
    x=(x0+x1)/2
    fx=fun(x)
    if fx*f1<0:
        x0=x
    else:
        x1=x
    if abs(fx)<0.01:
        break
    iteracion+=1    
print("La raiz es %.5f"%x0)
print("En",iteracion,"iteraciones")