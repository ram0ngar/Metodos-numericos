#ejemplo Bairstow
#f(x)=x^5-3.5x^4+2.75x^3+2.125x^2-3.875x+1.25
#[1.25,-3.87,2.125,2.75,-3.5,1]
def bn(a):
    return a[-1]
def bn1(a,b,c):
    return a[-2]+r*b

#(bn1,bn)
def bi(i,a,r,s,b):
    return a[i]++r*b[0]+s*b[1]

def cn(b):
    return bn(b)
def cn1(b,c,r):
    return bn1(b,c,r)
def ci(i,b,r,s,c):
    return bi(i,b,r,s,c)

r=-1
s=-1
b=[]
raices=[]
for i in range (100):
    b=[]
    c=[]
    b.append(bn([-998.46,464,-35.51,-8.6,1]))
    b.insert(0,bn1([-998.46,464,-35.51,-8.6,1],b[0],r))
    print(b)

    for i in reversed(range(0,3)):
        b.insert(0,bi(i,[-998.46,464,-35.51,-8.6,1],r,s,b))


    c.append(cn(b))
    c.insert(0,cn1(b,c[0],r))

    for i in reversed(range(0,3)):
        c.insert(0,ci(i,b,r,s,c))

    print(b)
    print(c)

    def deltaS(b,c):
        return (-b[1]/c[2]+b[0]/c[1])/(c[3]/c[2]-c[2]/c[1])
    def deltaR(b,c,dS):
        return -1*b[0]/c[1]-(c[2]/c[1])*dS
    dS=deltaS(b,c)
    dR=deltaR(b,c,dS)

    print(dS)
    print(dR)
    print("esta es r",r)
    print("esta es s",s)    

    if abs(dS)<0.01 and abs(dR)<0.01:
        break
    r=r+dR
    s=s+dS
#Calcular raices
#def cuadratica(r,s):