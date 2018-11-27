#Ejemplo
#x^2+y^2=10  u
#x^-y^2=1    v
def createMatrix(m,n,v):
    C=[]
    for i in range(m):
        C.append([])
        for j in range(n):
            C[i].append(v)
    return C

def getDimensions(A):
    return(len(A),len(A[0]))
    
    
def copyMatrix(B):
    m,n=getDimensions(B)
    A=createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            A[i][j]=B[i][j]
    return A
    
def sumMatrix(A,B):
    Am,An=getDimensions(A)
    Bm,Bn=getDimensions(B)
    if Am!=Bm or An!=Bn:
        print("Error las dimensiones deben ser iguales")
        return[]
    C=createMatrix(Am,An,0)
    for i in range(Am):
        for j in range (An):
            C[i][j]=A[i][j]+B[i][j]
    return C    

def restaMatrix(A,B):
    Am,An=getDimensions(A)
    Bm,Bn=getDimensions(B)
    if Am!=Bm or An!=Bn:
        print("Error las dimensiones deben ser iguales")
        return[]
    C=createMatrix(Am,An,0)
    for i in range(Am):
        for j in range (An):
            C[i][j]=A[i][j]-B[i][j]
    return C    

def multMatrix(A,B):
    Am,An=getDimensions(A)
    Bm,Bn=getDimensions(B)
    if An!=Bm:
        print("Error las dimensiones deben ser iguales")
        return[]
    C=createMatrix(Am,An,0)
    for i in range(Am):
        for j in range (Bn):
            C[i][j]=0
            for k in range(An):
                C[i][j]+=A[i][k]*B[k][j]
    return C    


def getAdyacente(A,r,c):
    Am,An=getDimensions(A)
    C=createMatrix(Am-1,An-1,0)
    for i in range(Am):
        if i==r:
            continue
        for j in range(An):
            if j==c:
                continue
            if(i<r):
                ci=i
            else:
                ci=i-1
            C[i][j]=A[i][j]
           
    return C

def detMatrix(A):
    m,n = getDimensions(A)
    if m!=n:
        print("Matriz no es cuadrada")
        return []
    if (n==1):
        return A[0][0]
    if (n==2):
        return (A[0][0]*A[1][1]) - (A[1][0]*A[0][1])
    det = 0
    for j in range(m):
        det += (-1)**j*A[0][j]*detMatrix(getAdyacente(A,0,j))
    return det

def getMatrizTranspuesta(A):
    m,n=getDimensions(A)
    C=createMatrix(n,m,0)
    for i in range(m):
        for j in range(n):
            C[j][i]=A[i][j]
    return C        

def getMatizAdjunta(A):
    m,n=getDimensions(A)
    if m !=n:
        print ("La matriz no es cuadrada")
        return[]
    C=createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j]=((-1)**(i+j))*detMatix(getAdyacente(A),i,j)
    return C        
    
def getInversa(A):
    m,n=getDimensions(A)
    if m!=n:
        print("La matriz no es cuadrada")
        return[]
    detA=detMatrix(A)
    if detA==0:
        print("La matriz no tiene inversa")
    At=getMatrizTranspuesta(A)
    adjA=getMatrizAdjunta(At)
    invDetA=1/detA
    C=createMatrix(m,n,0)
    for i in range(m):
        for j in range(n):
            C[i][j]=invDetA*adjA[i][j]
    return C        
    
A=createMatrix(6,6,0)
A[0]=[0.866,-0.5,0,0,0]
A[1]=[0.5,0,0.866,0,0,0]
A[2]=[-0.866,-1,0,-1,0,0]
A[3]=[-0.5,0,0,0,-1,0]
A[4]=[0,1,0.5,0,0,0]
A[5]=[0,0,-0.866,0,0,-1]
C=createMatrix(6,1,0)
C[1]=[-1000]
invA=getInversa(A)
B=multMatrix(invA,C)
print(B)




def dudx(x,y):
    return 2*x
def dudy(x,y):
    return 2*y
def dvdx(x,y):
    return 2*x
def dvdy(x,y):
    return -2*y

def u(x,y):
    return x**2+y**2-10

def v(x,y):
    return x**2-y**2-1

J=[[dudx],[dudy],[dvdx,dvdy]]
F=[[u],[v]]
B=[[1],[1]
  

E=0.01

for i in range(100):
    
    Ji=createMatrix(2,2,0)
    Jin,Jim=getDimensions(Ji)
    for k in range(Jin):
        for j in range(Jim):
            Ji[k][j]=J[k][j](B[0],B[1])
    
    Jinv=getMatrizInversa(Ji)
    Fi=createMatrix(2,1,0)
    for k in range(2):
        Fi[k][0]=F[k][0](B[0],B[1])
        
    Bi=B=restaMatrix(B,mulMatrix(Jinv,Fi))
    Be=restaMatrix(B,Bi)
   if abs(Be[0][0])<E and abs(Be[1][0]):
       B=Bi
       break
print("La solucion es",B)   