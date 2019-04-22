import numpy as np
import matplotlib. pyplot as plt
import cmath
M=32
import numpy as np
import matplotlib.pyplot as plt
m=32
n=np.arange(0,31)
y=[]
for i in range(0,31):
	x=1
	y=np.append(y,x)	
plt.stem(n,y)
plt.show()
wc=np.pi/4
m=np.arange(-100,100,1)
h=0.25*np.sinc(0.25*m)
k=np.arange(-17,17,1)
h1=0.25*np.sinc(0.25*k)
#plt.stem(m,h)
#plt.show()
def dtft(x):
	j=cmath.sqrt(-1)
	y=[]
	l=len(x)
	y=np.zeros(10000)
	w=np.linspace(-np.pi,np.pi,10000)
	for i in range(0,10000):
		sum=0
		for n in range(0,l):
			sum=sum+x[n]*(np.exp(-j*w[i]*n))
		y1=np.abs(sum)
		y=np.append(y,y1)
	print y
	return y
z=dtft(h)
#print z
#plt.plot(z)
#plt.show()
p=[]
for i in range(0,31):
	q=h1[i]*1
	p=np.append(p,q)

y0=dtft(p)
y1=20*np.log(y0)
plt.subplot(5,1,1)
plt.stem(n,y)
plt.subplot(5,1,2)
plt.stem(m,h)
plt.subplot(5,1,3)
plt.plot(z)
plt.subplot(5,1,4)
plt.plot(y0)
plt.subplot(5,1,5)
plt.plot(y1)
plt.show()
