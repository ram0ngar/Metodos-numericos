def getX1(x2,x3):
    return 16-x2-x3
def getX2(x1,x3):
    return 16.5-1.5*x1-1.5*x3
def getX3(x1,x2):
    return 16-2*x1-2*x2

#Valores inciales
x1=0
x2=0
x3=0
#x4=0
error=0.01
x1a=0.0001
x2a=0.0001
x3a=0.0001
#x4a=0.0001
for i in range(5):
    x1=getX1(x2,x3)
    x2=getX2(x1,x3)
    x3=getX3(x1,x2)
    #x4=getX4(x1,x2,x3)
    #print("itera %d"%i,x1,x2,x3)
    #Calculo de errores
    ex1=abs((x1a-x1)/x1a)
    ex2=abs((x2a-x2)/x2a)
    ex3=abs((x3a-x3)/x3a)
    if(ex1<error and ex2<error and ex3<error):
        break
    print("Los valores en la iteracion "+str(i)+" son: ",x1,x2,x3)    
    x1a=x1
    x2a=x2
    x3a=x3
    #x4a=x4
print("Error= ",error)    
print("Los valores son",x1,x2,x3)    
        
   