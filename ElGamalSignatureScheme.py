
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

def ElGamalKeyGeneration():
    P=[]
    p=int(input("Enter prime number: "))
    e1=int(input("Enter e1: "))
    x=sqmul(e1,p-2,p)
    for i in range(1,p-1):
    	if sqmul(e1,i,p)==1:
            print(e1," is not a primitive root of ",p)
            f.write(e1)
            f.write(" is not a primitive root of ")
            f.write(p)
            exit()
    if sqmul(e1,p-1,p) !=1:
        print(e1," is not a primitive root of ",p)
        f.write(e1)
        f.write(" is not a primitive root of ")
        f.write(p)
        exit()
    d=int(input("Enter private key: "))
    r=int(input("Enter r: "))
    rinv=EucledeanExtended(r,p-1)
    e2=sqmul(e1,d,p)
    P.append(e1)
    P.append(e2)
    P.append(p)
    return P,d,r

def EucledeanExtended(a, m) : 
    m0=m 
    y=0
    x=1
    if(m==1) : 
        return 0
    while (a>1) : 
    	if math.gcd(a,m)!=1:
            print("Inverse of r does not exist.")
            f.write("Inverse of r does not exist.")
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
    s1=sqmul(P[0],r,P[2])
    rinv=EucledeanExtended(r,P[2]-1)
    if rinv==False:
        return False,False
    t=(M-(d*s1)) * rinv
    s2=(t)%(P[2]-1)
    return s1,s2

def SignatureVerification(M,s1,s2,P):
    t1=sqmul(P[1],s1,P[2])
    t2=sqmul(s1,s2,P[2])
    v2=(t1*t2)%P[2]
    v1=sqmul(P[0],M,P[2])
    if v1==v2:
        return True,v1,v2
    else:
        return False,v1,v2

def main():
    P,d,r=ElGamalKeyGeneration()
    st=input("Enter message: ")
    print()
    print("Intermediate outputs: ")
    f.write("Intermediate outputs: \n")
    x=0
    l=list(st)
    for i in range(len(l)):
        print(i)
        M=ord(l[i])
        print("M = ",M)
        f.write("\nM = ")
        f.write(str(M))
        s1,s2=SignatureGeneration(M,P,d,r)
        print("S1 = ",s1," and S2 = ",s2)
        f.write("\nS1 = ")
        f.write(str(s1))
        f.write(" S2 = ")
        f.write(str(s2))
        v,v1,v2=SignatureVerification(M,s1,s2,P)
        print("V1 = ",v1," and V2 = ",v2)
        f.write("\nV1 = ")
        f.write(str(v1))
        f.write(" V2 = ")
        f.write(str(v2))
        print()
        if(v==False):
            print("Signature not verified")
            f.write("\nSignature not verified")
            exit()
    print("Final output: ")
    print("Signature Verified!")
    f.write("\nFinal output: ")
    f.write("\nSignature Verified!")


if __name__=='__main__':
	main()