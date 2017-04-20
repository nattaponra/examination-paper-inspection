#!/usr/bin/env python
 
import numpy as np
import pylab
 
class Cart_diff(object):
	"""docstring for Cart_diff"""
	def __init__(self, arg):
		super(Cart_diff, self).__init__()
		self.arg = arg
		
 	def main(self,LIST,name,Num):
		 
		fix=np.ones(Num)

		y=[]
		x=[]
		T=[]
		for i in range(Num):
			x.append(i+1)
		 	
			y.append(LIST[i])
		print y
		markerline, stemlines, baseline = pylab.stem(x, y ,bottom=0.5 )
		pylab.setp(markerline, 'markerfacecolor', 'b' )
		pylab.setp(baseline, 'color','g', 'linewidth', 2)

		pylab.lines = pylab.plot(x,0.6*fix,x,0.4*fix )
		pylab.setp(pylab.lines ,'color','r','linewidth',2)
		pylab.xlabel('Examination') 
		pylab.ylabel('Discrimination Level') 
		#plt.yticks(range(len(y)), T, size='small')
		 
		pylab.savefig('chart/{:>}.png'.format(name))
		#show()
		lines=[]
		pylab.clf()

 	def main_Show(self,LIST,name,Num):
		 
		fix=np.ones(Num)

		y=[]
		x=[]
		T=[]
		for i in range(Num):
			x.append(i+1)
		 
			y.append(LIST[i])
		 
		markerline, stemlines, baseline = pylab.stem(x, y  ,bottom=0.5 )
		pylab.setp(markerline, 'markerfacecolor', 'b' )
		pylab.setp(baseline, 'color','g', 'linewidth', 2)

		pylab.lines = pylab.plot(x,0.6*fix,x,0.4*fix )
		pylab.setp(pylab.lines ,'color','r','linewidth',2)
		pylab.xlabel('Examination') 
		pylab.ylabel('Discrimination Level') 
		#xticks(range(len(x)), T, size='small')
		 
		pylab.savefig('chart/{:>}.png'.format(name))
		pylab.show()
		lines=[]
		pylab.clf()

"""m=Cart_diff(0)
LL=[1,2,3,4,5,43,1,2,3,2,3]
m.main_Show(LL,"1",4)"""
