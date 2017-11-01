class PrePro:
	def __init__(self,start,end,min,max):
		self.start = start
		self.end = end
		self.min = min
		self.max = max
		self.Prunedstr = []
		self.Prunedlst = []

	def GenBranchs(self,current,end,min,max,past):
	# count = count+1
	# print(count)
		if current == end :
			past+''
			self.Prunedstr.append(past)
			past = ''
			return 1
		if current>end:
			past = ''
			return -1
		for i in range(min,max):
			pred = past + ','+str(i)
			self.GenBranchs(current+i, end, min, max,pred)
		return 0

	def Makelists(self):
		for i in range(len(self.Prunedstr)):
			temp = self.Prunedstr[i]
			temp = temp[1:]
			templst = [int(x) for x in temp.split(',')]
			self.Prunedlst.append(templst) #These are by definition all unique 

	def Prune(self):
		self.GenBranchs(self.start,self.end,self.min,self.max,'')
		self.Makelists()
		return(self.Prunedlst)
ST = PrePro(0,500,30,65)
Data=ST.Prune()
text_file = open("Output.txt_2", "w")
text_file.write(str(Data))
text_file.close()
    
