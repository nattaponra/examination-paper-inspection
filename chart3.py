import matplotlib.pyplot as plt
class Chart_distinguish(object):
	"""docstring for Chart_"""
	def __init__(self, arg):
		super(Chart_distinguish, self).__init__()
		self.arg = arg
	def main(self,v1,v2,v3,v4,v5,v6,v7):	

		# The slices will be ordered and plotted counter-clockwise.
		labels = 'Best', 'Better', 'Good', 'Medium','Low','Lowly','Can\'t'
		#sizes = [10, 10, 10, 10, 10, 10, 40]
		sizes = [v1,v2,v3,v4,v5,v6,v7]
		colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','yellowgreen', 'gold', 'lightskyblue' ]
		explode = (0, 0.1, 0, 0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

		plt.pie(sizes, explode=explode, labels=labels, colors=colors,
		        autopct='%1.1f%%', shadow=True, startangle=90)
		# Set aspect ratio to be equal so that pie is drawn as a circle.
		plt.axis('equal')
		plt.savefig('chart/foo1.png')
		#plt.show()

        