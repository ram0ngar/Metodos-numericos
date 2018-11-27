#Método Runge-Kutta 
# y' -xy = 0; y(0) = 1 ; y(2) = ?
# h= 0.5; h = 0.25
# y = e^(x^2/2)
import numpy as np
from math import exp
import matplotlib.pyplot as plt
x0 = 0
y0 = 1
xn = 2
h  = 0.5
f = lambda x,y: x*y
n = int(abs(x0-xn)/h) + 1
x = np.linspace(x0,xn,n)

def rk1(y0,h,f,x):
    y = []
    y.append(y0)
    for i in range(1,len(x)):
        y.append(y[i-1] + h * f(x[i-1],y[i-1]))
    return y

def rk2(y0,h,f,x):
    y = []
    y.append(y0)
    for i in range(1,len(x)):
        k1 = h * f(x[i-1],y[i-1])
        k2 = h * f(x[i-1] + h/2,y[i-1] + k1/2 )
        y.append(y[i-1] + k2)
    return y

def rk4(y0,h,f,x):
    y = []
    y.append(y0)
    for i in range(1,len(x)):
        k1 = h * f(x[i-1],y[i-1])
        k2 = h * f(x[i-1] + h/2,y[i-1] + k1/2 )
        k3 = h * f(x[i-1] + h/2,y[i-1] + k2/2 )
        k4 = h * f(x[i-1]  + h,y[i-1] + k3 )
        y.append(y[i-1] + 1/6*(k1 + 2*k2 + 2*k3 + k4))
    return y

plt.plot(x,rk1(y0,h,f,x),'r')
plt.plot(x,rk2(y0,h,f,x),'b')
plt.plot(x,rk4(y0,h,f,x),'y')
plt.plot(x,[exp(xi**2/2) for xi in x],'p')