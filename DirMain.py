import os

class dire(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(dire, self).__init__()
		self.arg = arg
	def create(self):	
		if not os.path.exists('image/process/'):
			os.makedirs('image/process/')

		if not os.path.exists('image/process/'):
			os.makedirs('image/process/')

		if not os.path.exists('image/sub/'):
			os.makedirs('image/sub/')

		if not os.path.exists('image/submain/'):
			os.makedirs('image/submain/')

		if not os.path.exists('image/input/'):
			os.makedirs('image/input/')

		if not os.path.exists('exam/'):
			os.makedirs('exam/')

		if not os.path.exists('inspected/'):
			os.makedirs('inspected/')
			os.makedirs('inspected/M1/')
			os.makedirs('inspected/M1/k1')
			os.makedirs('inspected/M1/k2')
			os.makedirs('inspected/M1/k3')
			os.makedirs('inspected/M1/k4')
			os.makedirs('inspected/M1/onekey')


			os.makedirs('inspected/M2/')
			os.makedirs('inspected/M2/k1')
			os.makedirs('inspected/M2/k2')
			os.makedirs('inspected/M2/k3')
			os.makedirs('inspected/M2/k4')
			os.makedirs('inspected/M2/onekey')

			os.makedirs('inspected/M3/')
			os.makedirs('inspected/M3/k1')
			os.makedirs('inspected/M3/k2')
			os.makedirs('inspected/M3/k3')
			os.makedirs('inspected/M3/k4')
			os.makedirs('inspected/M3/onekey')


			os.makedirs('inspected/SC/')
			os.makedirs('inspected/SC/k1')
			os.makedirs('inspected/SC/k2')
			os.makedirs('inspected/SC/k3')
			os.makedirs('inspected/SC/k4')
			os.makedirs('inspected/SC/onekey')

			os.makedirs('inspected/nokey')


		if not os.path.exists('distracter/'):
			os.makedirs('distracter/')
			os.makedirs('distracter/Sc/')
			os.makedirs('distracter/s1')
			os.makedirs('distracter/s2')
			os.makedirs('distracter/s3')
			os.makedirs('distracter/s4')
			
		if not os.path.exists('distracter/'):
			os.makedirs('distracter/')
			os.makedirs('distracter/Sc/')
			os.makedirs('distracter/s1')
			os.makedirs('distracter/s2')
			os.makedirs('distracter/s3')
			os.makedirs('distracter/s4')			 

		if not os.path.exists('keyimg/'):
			os.makedirs('keyimg/')

		if not os.path.exists('chart/'):
			os.makedirs('chart/')

		if not os.path.exists('key/'):
			os.makedirs('key/')

		if not os.path.exists('setting/'):
			os.makedirs('setting/')


			file = open("setting/format_tab1.txt", "w")
			file.write("0"+"\n")
			file.write("1"+"\n")		 
			file.write("1"+"\n")
			file.close() 

			file = open("setting/format_tab2.txt", "w")
			file.write("Yes"+"\n")
			file.write("1"+"\n")
			file.write("1"+"\n")
			file.write("No"+"\n")
			file.close() 


			file = open("setting/format_tab2_down.txt", "w")
			file.write("No"+"\n")
			file.write("###"+"\n"+"1Yes\n0\n0\n0\n1No\n")	
			file.write("###"+"\n"+"1Yes\n0\n0\n0\n1No\n")	
			file.write("###"+"\n"+"1Yes\n0\n0\n0\n1No\n")	
			file.close() 



			file = open("setting/format_tab3.txt", "w")
			file.write("No"+"\n")
			file.close() 


			file = open("setting/SelectKey.txt", "w")
			file.write("single"+"\n")
			file.write(" "+"\n")
	
			file.write("0"+"\n")
			file.close() 


			file = open("setting/setting.txt", "w")
			file.write("0"+"\n")
			file.write("1"+"\n")
			file.write("C:\Users\I'M CPE\Desktop"+"\n")
			file.write(".PNG"+"\n")
			file.close() 


		if not os.path.exists('key/'):
			os.makedirs('key/')


		if not os.path.exists('TR/'):
			os.makedirs('TR/')
m=dire(0)
m.create()