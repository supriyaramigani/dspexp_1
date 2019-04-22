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