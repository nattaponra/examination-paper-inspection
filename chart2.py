#!/usr/bin/env python
from pylab import *
import numpy as np
import random
import matplotlib.image as mpimg

 

fix=np.ones(120)

y=[]
x=[]
T=[]
for i in range(120):
	x.append(i)
 
	y.append(random.uniform(0, 1))
 
markerline, stemlines, baseline = stem(x, y  ,bottom=0.5   )
#setp(markerline, 'markerfacecolor', 'b' )
#setp(baseline, 'color','g', 'linewidth', 2)

lines = plot(x,0.6*fix,x,0.4*fix )
setp(lines ,'color','r','linewidth',2)
 
#plt.yticks(range(len(y)), T, size='small')
 
savefig('chart/foo.png')
show()