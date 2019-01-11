import time
import math

def fermatfactorization(n):
    x=int(n**0.5)+1
    while x<n:
        w=int(abs((x*x)-n))
        y=int(w**0.5)
        if (y*y)==w:
            a=x+y
            b=x-y
            return a,b
        x=x+1
    return 1,n

def pollardpminonefactorization(n,b):
    a=2
    e=2
    while e<=b:
        a=(a**e)%n
        e=e+1
    p=math.gcd(a-1,n)
    if p<n and p>1:
        return p
    return False


def f(k):
    return (k*k)+1


def pollardrhofactorization(n):
    x=2
    y=2
    p=1
    while p==1:
        x=(f(x))%n
        y=f(f(y)%n)%n
        p=math.gcd(abs(x-y),n)
    return p


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

def fermatprimalitytest(p):
    prime=True
    for i in [2,3,5,7,11]:
        if i>=p:
            break
        if sqmul(i,p-1,p)==1:
            continue
        else:
            prime=False
            break
    if p==1:
    	return False
    return prime


n=int(input("Enter a number: "))

print("By fermat factorization method: ")
t1=time.time()
x,y=fermatfactorization(n)
t2=time.time()
print("Time to derive factors is: ",(t2-t1))
t1=time.time()
p=fermatprimalitytest(x)
t2=time.time()
if p==True:
	print("Factor 1 is ",x, " and it is prime")
else:
	print("Factor 1 is ",x, " and it is not prime")
print("Time to verify primality for factor 1 is ",t2-t1)
t1=time.time()
p=fermatprimalitytest(y)
t2=time.time()
if p==True:
	print("Factor 2 is ",y, " and it is prime")
else:
	print("Factor 2 is ",y, " and it is not prime")
print("Time to verify primality for factor 2 is ",t2-t1)
print()
if x==1 or y==1:
	print("fermat method failed")
print()

print("By pollard p-1 factorization method: ")
t1=time.time()
for i in range(int(n**0.5)):
    x=pollardpminonefactorization(n,i)
    if x!=False:
        break;
t2=time.time()
if(x== False):
	x=n
	y=1
else:
	y=int(n/x)
print("Time to derive factors is: ",(t2-t1))
t1=time.time()
p=fermatprimalitytest(x)
t2=time.time()
if p==True:
	print("Factor 1 is ",x, " and it is prime")
else:
	print("Factor 1 is ",x, " and it is not prime")
print("Time to verify primality for factor 1 is ",t2-t1)
t1=time.time()
p=fermatprimalitytest(y)
t2=time.time()
if p==True:
	print("Factor 2 is ",y, " and it is prime")
else:
	print("Factor 2 is ",y, " and it is not prime")
print("Time to verify primality for factor 2 is ",t2-t1)
print()
if x==1 or y==1:
	print("pollard p-1 method failed")
print()

print("By pollard rho factorization method: ")
t1=time.time()
x=pollardrhofactorization(n)
t2=time.time()
y=int(n/x)
print("Time to derive factors is: ",(t2-t1))
t1=time.time()
p=fermatprimalitytest(x)
t2=time.time()
if p==True:
	print("Factor 1 is ",x, " and it is prime")
else:
	print("Factor 1 is ",x, " and it is not prime")
print("Time to verify primality for factor 1 is ",t2-t1)
t1=time.time()
p=fermatprimalitytest(y)
t2=time.time()
if p==True:
	print("Factor 2 is ",y, " and it is prime")
else:
	print("Factor 2 is ",y, " and it is not prime")
print("Time to verify primality for factor 2 is ",t2-t1)
print()
if x==1 or y==1:
	print("pollard rho method failed")
print()


'''
def millerrabin(n,a):
    k=0
    x=n-1
    while(x%2!=1):
        k=k+1
        x=x/2
    m=int(n/(2**k))
    t=(a**m)%n
    if t==1 or t==n-1:
        return True
    for i in range(1,k):
        t=(t*t)%n
        if t==1:
            return False
        if t==-1:
            return True
    return False
 '''

