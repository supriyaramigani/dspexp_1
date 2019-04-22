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
y=dft(x)
print y
x1=[4,1,2,3]
y1=dft(x1)
print y1
y2=[]
for k in range(0,4):
	s=np.exp(-j*2*np.pi*k/4)*y[k]
	y2=np.append(y2,s)
print y2

