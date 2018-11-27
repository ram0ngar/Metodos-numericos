#Eliminacion gaussiana
def createMatrix(m,n,v):
    C = []
    for i in range(m):
        C.append([v]*n)
    return C

MA = createMatrix(3,4,0)
MA[0] = [1,-3,0,100]
MA[1] = [-2,0,1,-200]
MA[2] = [1,1,1,1100]
#MA[3] = [1,-1,4,3,4]

for i in range(3):
    pivote = MA[i][i]
    if pivote == 0:
        for j in range(i+1,3):
            if MA[j][i] != 0:
                T = MA[j]
                MA[j] = MA[i]
                MA[i] = T
                pivote = MA[i][i]
                break
    for k in range(4):
        MA[i][k] = (1/pivote)*MA[i][k]
    for j in range(i+1,3):
        C = -1* MA[j][i]
        T = createMatrix(1,4,0)
        for k in range(4):
            T[0][k] = C*MA[i][k]
        for k in range(4):
            MA[j][k] += T[0][k]
print(MA)

B = createMatrix(3,1,0)
for i in range(2,-1,-1):
    B[i][0] = MA[i][3]
    for j in range(2,-1,-1):
        if i == j:
            break
        B[i][0] -= MA[i][j]*B[j][0]
        
print(B)
 