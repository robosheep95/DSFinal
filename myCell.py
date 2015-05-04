class myCell():
	def __init__(self):
		self.pos = []
		self.x = 0
		self.y = 0
	
	def setRow(self, x):
		self.x = x
	
	def setCol(self, y):
		self.y = y
		
	def getRow(self):
		return self.x
	
	def getCol(self):
		return self.y
		
	def getBox(self, box):
		self.box = box
	
	def setBox(self):
		return self.box
		
	def getPos(self):
		return self.pos
	
	def __add__(self, inp):
		if inp != in self.pos:
			self.pos.append(inp)
		else:
			pass
	
	def __sub__(self, inp):
		if inp == in self.pos:
			self.pos.remove(inp)
		else:
			pass
		
		
