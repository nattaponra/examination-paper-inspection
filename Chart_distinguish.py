
class Chart_distinguish(object):
	import matplotlib.pyplot as PLT
	"""docstring for Chart_"""
	def __init__(self, arg):
		super(Chart_distinguish, self).__init__()
		self.arg = arg
	def Main(self,v1,v2,v3,v4,v5,v6,v7,nameF):	
		m_pie = None
 		m_pie = self.PLT
		# The slices will be ordered and plotted counter-clockwise.
		labels = 'Best', 'Better', 'Good', 'Medium','Low','Lowly','Can\'t'
		#sizes = [10, 10, 10, 10, 10, 10, 40]
		 
		sizes = [v1,v2,v3,v4,v5,v6,v7]
		colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red', 'green', 'blue' ]
		explode = (0.2, 0, 0, 0, 0, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

		m_pie.pie(sizes, explode=explode, labels=labels, colors=colors,
		        autopct='%1.1f%%', shadow=True, startangle=190)
		# Set aspect ratio to be equal so that pie is drawn as a circle.
		#PLT.axis('equal')
		m_pie.savefig('chart/{:>}.png'.format(nameF))
		m_pie.clf()
 		sizes=[]
 		labels=[]
		#PLT.show()
	def Main_Show(self,v1,v2,v3,v4,v5,v6,v7,nameF):	
		m_pie = None
 		m_pie = self.PLT
		# The slices will be ordered and plotted counter-clockwise.
		labels = 'Best', 'Better', 'Good', 'Medium','Low','Lowly','Can\'t'
		#sizes = [10, 10, 10, 10, 10, 10, 40]
		 
		sizes = [v1,v2,v3,v4,v5,v6,v7]
		colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red', 'green', 'blue' ]
		explode = (0.2, 0, 0, 0, 0, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

		m_pie.pie(sizes, explode=explode, labels=labels, colors=colors,
		        autopct='%1.1f%%', shadow=True, startangle=190)
		# Set aspect ratio to be equal so that pie is drawn as a circle.
		#PLT.axis('equal')
		m_pie.savefig('chart/{:>}.png'.format(nameF))
		
 		sizes=[]
 		labels=[]
		self.PLT.show()
 		m_pie.clf()
"""m1=Chart_distinguish(1)  
  m1.Main(10, 10, 10, 10, 10,  0, 50,"c1") 
  m2=Chart_distinguish(0)
  m2.Main_Show(50, 10, 10, 10, 10,  0, 10,"c2")"""  
 