#ejemplo de convergencia
import matplotlib.pyplot as plt
def xnew(xprev):
    return (2*xprev^2+3)/5
x0=0
iteraciones=0
x1=0
x0array=[]
x1array=[]
for i in range(10):
    x1=xnew(x0)
    x0array.append(x0)
    x1array.append(x1)
    if abs(x1-x0)<0.0001:
        break
    x0=x1
    iteraciones +=1

print("La raiz es %.5f"%x1)
print("Numero de iteraciones %d"%iteraciones)

plt.plot(x0array,x1array)
plt.grid()