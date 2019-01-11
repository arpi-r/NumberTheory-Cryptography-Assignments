import hashlib
import math
f=open("output.txt","w")

def sqmul(a,x,n):
    x=bin(x)
    x=list(x)
    x=x[2:]
    y=1
    for i in range(len(x)-1,-1,-1):
        if int(x[i])==1:
            y=(a*y)%n
        a=(a*a)%n
    return y

def DSSKeyGeneration():
    P=[]
    p=int(input("Enter prime number p: "))
    q=int(input("Enter prime number q: "))
    e0=int(input("Enter e0: "))
    x=sqmul(e0,p-2,p)
    for i in range(1,p-1):
        if sqmul(e0,i,p)==1:
            print(e0," is not a primitive root of ",p)
            f.write(str(e0))
            f.write(" is not a primitive root of ")
            f.write(str(p))
            exit()
    if sqmul(e0,p-1,p) !=1:
        print(e0," is not a primitive root of ",p)
        f.write(str(e0))
        f.write(" is not a primitive root of ")
        f.write(str(p))
        exit()

    t=(p-1)//q
    e1=sqmul(e0,t,p)
    d=int(input("Enter private key d: "))
    e2=sqmul(e1,d,p)
    EucledeanExtended(e2,q)
    r=int(input("Enter r: "))
    if r>=q:
        print("r is greater than q")
        f.write("r is greater than q")
        exit(0)
    EucledeanExtended(r,q)
    P.append(e1)
    P.append(e2)
    P.append(p)
    P.append(q)
    return P,d,r

def EucledeanExtended(a, m) : 
    m0=m 
    y=0
    x=1
    if(m==1) : 
        return 0
    while (a>1) : 
        if math.gcd(a,m)!=1:
            print("Inverse does not exist.")
            f.write("Inverse does not exist.")
            exit()
        q=a//m 
        t=m
        m=a%m
        a=t
        t=y 
        y=x-q*y
        x=t 
    if (x<0): 
        x=x+m0 
    return x

def SignatureGeneration(M,P,d,r):
    s1=sqmul(P[0],r,P[2])%P[3]
    x=EucledeanExtended(r,P[3])
    s2=(((M+(d*s1))%P[3])*(x%P[3]))%P[3]
    return s1,s2

def SignatureVerification(M,s1,s2,P):
    s2inv=EucledeanExtended(s2,P[3])
    t1=M*s2inv
    t2=s1*s2inv
    v=sqmul(P[0],t1,P[2])*sqmul(P[1],t2,P[2])
    v=(v%P[2])%P[3]
    if (s1)==(v):
        return True,v
    else:
        return False,v

def main():
    P,d,r=DSSKeyGeneration()
    M=int(input("Enter message: "))
    f.write("\n")
    print("h(M) = ",M)
    f.write("\nh(M) = ")
    f.write(str(M))
    print("p = ",P[2])
    f.write("\np = ")
    f.write(str(P[2]))
    print("q = ",P[3])
    f.write("\nq = ")
    f.write(str(P[3]))
    print("e1 = ",P[0])
    f.write("\ne1 = ")
    f.write(str(P[0]))
    print("e2 = ",P[1])
    f.write("\ne2 = ")
    f.write(str(P[1]))
    s1,s2=SignatureGeneration(M,P,d,r)
    print("S1 = ",s1," and S2 = ",s2)
    f.write("\nS1 = ")
    f.write(str(s1))
    f.write(" S2 = ")
    f.write(str(s2))
    tf,v=SignatureVerification(M,s1,s2,P)
    print("V = ",v)
    f.write("\nV = ")
    f.write(str(v))
    print()
    if(tf==False):
        print("Signature not verified")
        f.write("\nSignature not verified")
        exit()
    print("Signature verified!!") 
    f.write("\nSignature verified!!")       

if __name__=='__main__':
    main()
