#Newton
def f(c):
    return c**4-8.6*(c**3)-35.51*(c**2)+464*c-998.46
def fprima(c):
    return 4*(c**3)-25.8*(c**2)-71.02*c+464
x0=2
itera=0
for i in range(100):
    itera+=1
    xr=x0-(f(x0)/fprima(x0))
    fxr=f(xr)
    if abs(fxr)<0.01:
        break
    x0=xr
print("El valor de la raiz es %0.5f"%x0)
print("Numero de iteraciones %i"%itera)