import random
from matplotlib import pyplot as plt
import numpy as np
T=  []
X1=  []
Y1 = []
X2=  []
Y2 = []

for i in range(50):
	T.append(str(i)+"A")
	X1.append(i)
	Y1.append(random.uniform(0, 1))

	X2.append(i)
	Y2.append(random.uniform(0, 1))
with plt.style.context('fivethirtyeight'):
	 plt.xticks(range(len(X1)), T, size='small')
	 plt.plot(X1,Y1)
 	 plt.plot(X2,Y2)    

plt.show() 


 
