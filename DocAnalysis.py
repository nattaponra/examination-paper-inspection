import sys
sys.path.append( '..' )
 
from PyRTF import *
class Doc(object):
	"""docstring for Doc"""



	def __init__(self, arg):
		super(Doc, self).__init__()
		self.arg = arg


	def Calcul(self,Value):
		message=""
		if Value<=0.05:
			message="No"
		elif  Value<0.5 and Value>0.05:
			message="Medium"
		elif  Value>=0.5 and Value<=1:
			message="Good"
		elif Value==10:
			message="Answer"
		return message
	def get_location(self):
		file = open("setting/setting.txt", "r")
		list_answer=file.readlines() 
 		file.close
 		return list_answer[2].strip()
	def Convert(self,List):
            diff=""

            if List=="ve":
                diff="Very Easy"
            elif List=="e":
                diff="Easy"
            elif List=="m":
                diff="Medium"
            elif List=="c":
                diff="Difficult"
            elif List=="vc":
                diff="Very Difficult"	
            return diff
	def Difficulty(self,num,LIST1,LIST2,LIST3,LIST4,Level_1,Level_2,Level_3,Level_4,v1,v2,v3,v4,All1,All2,All3,All4) :
		# another test for the merging of cells in a document
		
		doc = Document()
		section = Section()
		doc.Sections.append( section )

		# create the table that will get used for all of the "bordered" content

		col1 = 2000
		col2 = 2000
		col3 = 2000
		col4 = 2000
		col5 = 2000
		thin_edge  = BorderPS( width=20, style=BorderPS.SINGLE )
		thick_edge = BorderPS( width=80, style=BorderPS.SINGLE )
		thin_frame  = FramePS( thin_edge,  thin_edge,  thin_edge,  thin_edge )
		#section.append( ' Difficulty Table' )
		if LIST1!=[]:
			section.append( ' ' )
			section.append( '                                   Key 1'  )
			table = Table( col1, col2, col3  ,col4)
			table.AddRow( Cell( Paragraph( 'Number' ), thin_frame ), Cell( Paragraph( 'Correct' ), thin_frame ), Cell( Paragraph( 'Incorrect' ), thin_frame ) ,Cell( Paragraph( 'level' ), thin_frame ))
			for i in range(len(LIST1)):
		 		table.AddRow( Cell( Paragraph( str(i+1) ), thin_frame ), Cell( Paragraph( str(LIST1[i] ) ), thin_frame ), Cell( Paragraph( str(All1-int(LIST1[i])) ), thin_frame ) , Cell( Paragraph( "("+str(v1[i])+") "+str(self.Convert(Level_1[i])) ), thin_frame ) )
		 	section.append(table)
		if LIST2!=[]:
			table = Table( col1, col2, col3  ,col4)
			section.append( ' ' )
			section.append( '                                   Key 2'  )
			
			table.AddRow( Cell( Paragraph( 'Number' ), thin_frame ), Cell( Paragraph( 'Correct' ), thin_frame ), Cell( Paragraph( 'Incorrect' ), thin_frame ) ,Cell( Paragraph( 'level' ), thin_frame ))
			for i in range(len(LIST2)):
		 		table.AddRow( Cell( Paragraph( str(i+1) ), thin_frame ), Cell( Paragraph( str(LIST2[i] ) ), thin_frame ), Cell( Paragraph(str(All2-int(LIST2[i]))), thin_frame ) , Cell( Paragraph("("+str(v2[i])+") "+str(self.Convert(Level_2[i]) )), thin_frame ) )
		 	section.append(table)
		if LIST3!=[]:
			table = Table( col1, col2, col3  ,col4)
			section.append( ' ' )
			section.append( '                                   Key 3'  )
			
			table.AddRow( Cell( Paragraph( 'Number' ), thin_frame ), Cell( Paragraph( 'Correct' ), thin_frame ), Cell( Paragraph( 'Incorrect' ), thin_frame ) ,Cell( Paragraph( 'level' ), thin_frame ))
			for i in range(len(LIST3)):
		 		table.AddRow( Cell( Paragraph( str(i+1) ), thin_frame ), Cell( Paragraph( str(LIST3[i] ) ), thin_frame ), Cell( Paragraph(str(All3-int(LIST3[i]))), thin_frame ) , Cell( Paragraph("("+str(v3[i])+") "+str(self.Convert(Level_3[i]))), thin_frame ) )
		 	section.append(table)
		if LIST4!=[]:
			table = Table( col1, col2, col3  ,col4)
			section.append( ' ' )
			section.append( '                                   Key 4'  )
			
			table.AddRow( Cell( Paragraph( 'Number' ), thin_frame ), Cell( Paragraph( 'Correct' ), thin_frame ), Cell( Paragraph( 'Incorrect' ), thin_frame ) ,Cell( Paragraph( 'level' ), thin_frame ))
			for i in range(len(LIST4)):
		 		table.AddRow( Cell( Paragraph( str(i+1) ), thin_frame ), Cell( Paragraph( str(LIST4[i] ) ), thin_frame ), Cell( Paragraph(str(All4-int(LIST4[i]))), thin_frame ) , Cell( Paragraph("("+str(v4[i])+") "+str(self.Convert(Level_4[i]) )), thin_frame ) )
		 	section.append(table)

 

	 	renderer = Renderer()
	 	renderer.Write( doc, file('{:>}/Difficulty.doc'.format(self.get_location()), 'w' ) )
	 
	def Distinguish(self,L1,L2,L3,L4,H1,H2,H3,H4,CH1,CH2,CH3,CH4,CL1,CL2,CL3,CL4,F1,F2,F3,F4):

		doc = Document()
		section = Section()
		doc.Sections.append( section )

		# create the table that will get used for all of the "bordered" content

		col1 = 2000
		col2 = 2000
		col3 = 2000
		col4 = 2000
		col5 = 2000
		thin_edge  = BorderPS( width=20, style=BorderPS.SINGLE )
		thick_edge = BorderPS( width=80, style=BorderPS.SINGLE )
		thin_frame  = FramePS( thin_edge,  thin_edge, thin_edge, thin_edge)

		if H1!=[] :
			section.append('Distinguish KEY 1')

			table = Table( col1, col2, 100  ,col4,col5)
			#table.AddRow( Cell( Paragraph( 'A-one',thin_frame), span=5 ) )
			table.AddRow( Cell( Paragraph( 'High Group' ), thin_frame ), Cell(  ''), Cell(  '' ) ,Cell( Paragraph( 'LOW Group' ), thin_frame ), Cell(  '' ))
			table.AddRow( Cell( Paragraph( 'STUDENT ID' ), thin_frame ), Cell( Paragraph( 'SCORE' ), thin_frame ), Cell(  '' ) ,Cell( Paragraph( 'STUDENT ID' ), thin_frame ), Cell( Paragraph( 'SCORE' ), thin_frame ))
			for i in range(len(H1)):
				 table.AddRow( Cell( Paragraph( str(H1[i][2]) ), thin_frame ), Cell( Paragraph( str(H1[i][0]) ), thin_frame ), Cell(  '') , Cell( Paragraph( str(L1[i][2])), thin_frame ) , Cell( Paragraph( str(L1[i][0]) ), thin_frame ))
		 
			section.append(table)
			section.append('')


			table = Table( col1, col2, col3  ,col4)
			table.AddRow( Cell( Paragraph( 'Number' ), thin_frame ), Cell( Paragraph( 'Correct/HIGH' ), thin_frame ), Cell( Paragraph( 'Incorrect/LOW' ), thin_frame ) ,Cell( Paragraph( 'Distinguish Level' ), thin_frame ))
			for i in range(10):
				 table.AddRow( Cell( Paragraph( str(i+1) ), thin_frame ), Cell( Paragraph( str(CH1[i]) ), thin_frame ), Cell( Paragraph( str(CL1[i]) ), thin_frame ) , Cell( Paragraph( str(F1[i]) ), thin_frame ) )
		 
			section.append(table)

		if H2!=[] :
			section.append('Distinguish KEY 2')

			table = Table( col1, col2, 100  ,col4,col5)
			#table.AddRow( Cell( Paragraph( 'A-one',thin_frame), span=5 ) )
			table.AddRow( Cell( Paragraph( 'High Group' ), thin_frame ), Cell(  ''), Cell(  '' ) ,Cell( Paragraph( 'LOW Group' ), thin_frame ), Cell(  '' ))
			table.AddRow( Cell( Paragraph( 'STUDENT ID' ), thin_frame ), Cell( Paragraph( 'SCORE' ), thin_frame ), Cell(  '' ) ,Cell( Paragraph( 'STUDENT ID' ), thin_frame ), Cell( Paragraph( 'SCORE' ), thin_frame ))
			for i in range(len(H2)):
				 table.AddRow( Cell( Paragraph( str(H2[i][2]) ), thin_frame ), Cell( Paragraph( str(H2[i][0]) ), thin_frame ), Cell(  '') , Cell( Paragraph( str(L2[i][2])), thin_frame ) , Cell( Paragraph( str(L2[i][0]) ), thin_frame ))
		 
			section.append(table)
			section.append('')

			table = Table( col1, col2, col3  ,col4)
			table.AddRow( Cell( Paragraph( 'Number' ), thin_frame ), Cell( Paragraph( 'Correct/HIGH' ), thin_frame ), Cell( Paragraph( 'Incorrect/LOW' ), thin_frame ) ,Cell( Paragraph( 'Distinguish Level' ), thin_frame ))
			for i in range(10):
				 table.AddRow( Cell( Paragraph( str(i+1) ), thin_frame ), Cell( Paragraph( str(CH2[i]) ), thin_frame ), Cell( Paragraph( str(CL2[i]) ), thin_frame ) , Cell( Paragraph( str(F2[i]) ), thin_frame ) )
		 
			section.append(table)


		if H3!=[] :
			section.append('Distinguish KEY 3')

			table = Table( col1, col2, 100  ,col4,col5)
			#table.AddRow( Cell( Paragraph( 'A-one',thin_frame), span=5 ) )
			table.AddRow( Cell( Paragraph( 'High Group' ), thin_frame ), Cell(  ''), Cell(  '' ) ,Cell( Paragraph( 'LOW Group' ), thin_frame ), Cell(  '' ))
			table.AddRow( Cell( Paragraph( 'STUDENT ID' ), thin_frame ), Cell( Paragraph( 'SCORE' ), thin_frame ), Cell(  '' ) ,Cell( Paragraph( 'STUDENT ID' ), thin_frame ), Cell( Paragraph( 'SCORE' ), thin_frame ))
			for i in range(len(H3)):
				 table.AddRow( Cell( Paragraph( str(H3[i][2]) ), thin_frame ), Cell( Paragraph( str(H3[i][0]) ), thin_frame ), Cell(  '') , Cell( Paragraph( str(L3[i][2])), thin_frame ) , Cell( Paragraph( str(L3[i][0]) ), thin_frame ))
		 
			section.append(table)
			section.append('')

			table = Table( col1, col2, col3  ,col4)
			table.AddRow( Cell( Paragraph( 'Number' ), thin_frame ), Cell( Paragraph( 'Correct/HIGH' ), thin_frame ), Cell( Paragraph( 'Incorrect/LOW' ), thin_frame ) ,Cell( Paragraph( 'Distinguish Level' ), thin_frame ))
			for i in range(10):
				 table.AddRow( Cell( Paragraph( str(i+1) ), thin_frame ), Cell( Paragraph( str(CH3[i]) ), thin_frame ), Cell( Paragraph( str(CL3[i]) ), thin_frame ) , Cell( Paragraph( str(F3[i]) ), thin_frame ) )
		 
			section.append(table)


		if H4!=[] :
			section.append('Distinguish KEY 4')

			table = Table( col1, col2, 100  ,col4,col5)
			#table.AddRow( Cell( Paragraph( 'A-one',thin_frame), span=5 ) )
			table.AddRow( Cell( Paragraph( 'High Group' ), thin_frame ), Cell(  ''), Cell(  '' ) ,Cell( Paragraph( 'LOW Group' ), thin_frame ), Cell(  '' ))
			table.AddRow( Cell( Paragraph( 'STUDENT ID' ), thin_frame ), Cell( Paragraph( 'SCORE' ), thin_frame ), Cell(  '' ) ,Cell( Paragraph( 'STUDENT ID' ), thin_frame ), Cell( Paragraph( 'SCORE' ), thin_frame ))
			for i in range(len(H4)):
				 table.AddRow( Cell( Paragraph( str(H4[i][2]) ), thin_frame ), Cell( Paragraph( str(H4[i][0]) ), thin_frame ), Cell(  '') , Cell( Paragraph( str(L4[i][2])), thin_frame ) , Cell( Paragraph( str(L4[i][0]) ), thin_frame ))
		 
			section.append(table)
			section.append('')

			table = Table( col1, col2, col3  ,col4)
			table.AddRow( Cell( Paragraph( 'Number' ), thin_frame ), Cell( Paragraph( 'Correct/HIGH' ), thin_frame ), Cell( Paragraph( 'Incorrect/LOW' ), thin_frame ) ,Cell( Paragraph( 'Distinguish Level' ), thin_frame ))
			for i in range(10):
				 table.AddRow( Cell( Paragraph( str(i+1) ), thin_frame ), Cell( Paragraph( str(CH4[i]) ), thin_frame ), Cell( Paragraph( str(CL4[i]) ), thin_frame ) , Cell( Paragraph( str(F4[i]) ), thin_frame ) )
		 
			section.append(table) 


		renderer = Renderer()
		renderer.Write( doc, file('{:>}/Distinguish.doc'.format(self.get_location()), 'w' ))	
	 
	def Distracter(self,main1,main2,main3,main4,High1,High2,High3,High4,Low1,Low2,Low3,Low4):

		doc = Document()
		section = Section()
		doc.Sections.append( section )

		# create the table that will get used for all of the "bordered" content
		print "|||",len(High1)
		col1 = 2000
		col2 = 2000
		col3 = 2000
		col4 = 2000
		col5 = 2000
		thin_edge  = BorderPS( width=20, style=BorderPS.SINGLE )
		thick_edge = BorderPS( width=80, style=BorderPS.SINGLE )
		thin_frame  = FramePS( thin_edge,  thin_edge,  thin_edge,  thin_edge )

		if main1!=[]:
			section.append( ' Distracter KEY 1'  )

			table = Table( 1200, 1200, 1200 ,1200,1200,1200,1200)
			#table.AddRow( Cell( Paragraph( 'A-one',thin_frame), span=5 ) ) 
			table.AddRow( Cell( Paragraph( 'HIGH Group' ), thin_frame ,span=7))
			table.AddRow( Cell( Paragraph( 'Number' ), thin_frame ), Cell( Paragraph( 'Choice1' ), thin_frame ), Cell( Paragraph(  'Choice2' ) ,thin_frame),Cell( Paragraph( 'Choice3' ), thin_frame ), Cell( Paragraph( 'Choice4' ), thin_frame ), Cell( Paragraph( 'Choice5' ), thin_frame ),Cell( Paragraph( 'Answer' ), thin_frame ))
			for j in range(len(High1)):
				table.AddRow( Cell( Paragraph( str(j+1) ), thin_frame ), Cell( Paragraph( str(High1[j][0]) ), thin_frame ), Cell( Paragraph( str(High1[j][1])) ,thin_frame),Cell( Paragraph( str(High1[j][2]) ), thin_frame ), Cell( Paragraph( str(High1[j][3]) ), thin_frame ), Cell( Paragraph( str(High1[j][4]) ), thin_frame ), Cell( Paragraph( str("") ) , thin_frame ))
			section.append(' ')
			section.append(table)


			table = Table( 1200, 1200, 1200 ,1200,1200,1200,1200)
			table.AddRow( Cell( Paragraph( 'LOW Group' ), thin_frame ,span=7))
			table.AddRow( Cell( Paragraph( 'Number' ), thin_frame ), Cell( Paragraph( 'Choice1' ), thin_frame ), Cell( Paragraph(  'Choice2' ) ,thin_frame),Cell( Paragraph( 'Choice3' ), thin_frame ), Cell( Paragraph( 'Choice4' ), thin_frame ), Cell( Paragraph( 'Choice5' ), thin_frame ),Cell( Paragraph( 'Answer' ), thin_frame ))
			for j in range(len(Low1)):
				table.AddRow( Cell( Paragraph( str(j+1) ), thin_frame ), Cell( Paragraph( str(Low1[j][0]) ) , thin_frame ), Cell( Paragraph( str(Low1[j][1]) )  ,thin_frame),Cell( Paragraph( str(Low1[j][2])), thin_frame ), Cell( Paragraph( str(Low1[j][3]))  , thin_frame ), Cell( Paragraph( str(Low1[j][4])), thin_frame ), Cell( Paragraph( str("") ), thin_frame ))
			section.append(' ')
			section.append(table)

			table = Table( 1200, 1200, 1200 ,1200,1200,1200 )
 			table.AddRow( Cell( Paragraph( 'Distracter' ), thin_frame ,span=6))
			table.AddRow( Cell( Paragraph( 'Number' ), thin_frame ), Cell( Paragraph( 'Choice1' ), thin_frame ), Cell( Paragraph(  'Choice2' ) ,thin_frame),Cell( Paragraph( 'Choice3' ), thin_frame ), Cell( Paragraph( 'Choice4' ), thin_frame ), Cell( Paragraph( 'Choice5' ), thin_frame ))
			for j in range(len(main1)):
				table.AddRow( Cell( Paragraph( str(j+1) ), thin_frame ), Cell( Paragraph( str(self.Calcul(main1[j][0]))), thin_frame ), Cell( Paragraph( str(self.Calcul(main1[j][1]))) ,thin_frame),Cell( Paragraph( str(self.Calcul(main1[j][2]))), thin_frame ), Cell( Paragraph(str(self.Calcul(main1[j][3]))), thin_frame ), Cell( Paragraph( str(self.Calcul(main1[j][4]))), thin_frame ))
			 
			section.append(' ')	
			section.append(table)
		renderer = Renderer()
		renderer.Write( doc, file('{:>}/Distracter.doc'.format(self.get_location()), 'w' ) )
"""Li1=[]
Li1.append((1,1,1,1))
Li1.append((1,2,3,4))
Li1.append((1,2,3,4))
Li1.append((1,2,3,4))

Li2=[]
Li2.append((2,2,2,2))
Li2.append((1,2,3,4))
Li2.append((1,2,3,4))
Li2.append((1,2,3,4))

Li3=[]
Li3.append((3,3,3,3))
Li3.append((1,2,3,4))
Li3.append((1,2,3,4))
Li3.append((1,2,3,4))

Li4=[]
Li4.append((4,4,4,4))
Li4.append((1,2,3,4))
Li4.append((1,2,3,4))
Li4.append((1,2,3,4))
M=Doc(0)
M.Difficulty(2,Li1,Li2,Li3,Li4)"""