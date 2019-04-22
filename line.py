import numpy as np
import cmath
def dft(x):
	y=[]
	j=cmath.sqrt(-1)
	N=len(x)
	for k in range (0,N):
		sum=0
		for n in range (0,N):
			sum=sum+(x[n]*np.exp(-j*2*np.pi*n*k/N))
		y=np.append(y,sum)
	print y
	return y
x1=input("enter sequence one:")
y1=dft(x1)
x2=input("enter sequence two:")
y2=dft(x2)
m=len(x1)
n=len(x2)
q=max(m,n)
x=[]
for i in range(0,q):
	x3=x1[i]+x2[i]
	x=np.append(x,x3)
y=dft(x)
print "y1=",y1
print "y2=",y2
print "y=",y
f=[]
for i in range(0,len(y)):
	f1=y1[i]+y2[i]
	f=np.append(f,f1)
print"f=",f
	