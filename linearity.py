import matplotlib.pyplot as plt
import numpy as np
import cmath as cm
def dft(x):
    
    
    j=cm.sqrt(-1)
    y=[]
    n=len(x)
    for k in range(0,n):
	w_1=((2*np.pi/n))
	sum=0
        for i in range(0,n):
            sum=sum+(x[i]*np.exp(-k*w_1*j*i))
        y.append(sum)
       
    return y
x1=input("enter the values of x1:")
x2=input("enter the values of x2:")
y=[]
t1=[]
t2=[]
t3=[]
t4=[]
m=len(x1)
n=len(x2)
q=max(m,n)
for i in range(0,q,1):
	p1=x1[i]+x2[i]
	y.append(p1)
t1=dft(x1)
t2=dft(x2)
t3=dft(y)
for i in range(0,len(t1),1):
	p2=t1[i]+t2[i]
	t4.append(p2)
print(t1)
print(t2)
print(t3)
plt.subplot(411)
plt.stem(t1)
plt.subplot(412)
plt.stem(t2)
plt.subplot(413)
plt.stem(t3)
plt.subplot(414)
plt.stem(t4)
plt.show()


