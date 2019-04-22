import numpy as np
import cmath
j=cmath.sqrt(-1)
def dft(x):
	y=[]
	j=cmath.sqrt(-1)
	N=len(x)
	for k in range (0,N):
		sum=0
		for n in range (0,N):
			sum=sum+(x[n]*np.exp(-j*2*np.pi*n*k/N))
		y=np.append(y,sum)
	
	return y
x=[1,2,3,4]
h=[0,1,3,4]
y1=dft(x)
y2=dft(h)
y3=[]
for k in range(0,4):
	s=y1[k]*y2[k]
	y3=np.append(y3,s)
print y3
y=[]
for n in range(0,7):
	sum=0
	for m in range(0,4):
		if(n-m>=0 and n-m<4):
			sum=sum+x[m]*h[n-m]
	y=np.append(y,sum)
print y
z1=[]
for i in range(4,7):
	z=y[i]+y[i-4]
	z1=np.append(z1,z)
w=y[3]
z1=np.append(z1,w)
print z1
z2=dft(z1)
print z2
	
