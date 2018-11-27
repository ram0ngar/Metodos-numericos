def xnew(xprev):
    return (2*xprev^2+3)/5
x0=0
iteraciones=1
x0=0
for i in range(100):
    x1=xnew(x0)
    if abs(x1-x0)<0.0001:
        break
    x0=x1
    iteraciones +=1

print("La raiz es %.5f"%x1)
print("Numero de iteraciones %d"%iteraciones)