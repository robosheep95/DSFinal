class myCell():
    def __init__(self):
        self.pos = []
        self.col = 0
        self.row = 0
        self.box = 0
        self.answer = 0

    def setRow(self, x):
        self.row = x
    
    def setCol(self, y):
        self.col = y
            
    def getRow(self):
        return self.row
    
    def getCol(self):
        return self.col
            
    def setBox(self, box):
        self.box = box
    
    def getBox(self):
        return self.box
    
    def setAnswer(self,value):
        self.answer = value
            
    def getAnswer(self):
        return self.answer
            
    def getPos(self):
        return list(self.pos)

    def setPos(self,inp):
        self.pos = inp
    
    def addPos(self,inp):
        if inp not in self.pos:
            self.pos.append(inp)
        else:
            pass
    
    def removePos(self, inp):
        if inp in self.pos:
            self.pos.remove(inp)
        else:
            pass

    def getLen(self):
        return len(self.getPos())
