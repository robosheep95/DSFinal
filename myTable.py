from myCell import *

##01 02 03 04 05 06 07 08 09
##10 11 12 13 14 15 16 17 18
##19 20 21 22 23 24 25 26 27
##28 29 30 31 32 33 34 35 36
##37 38 39 40 41 42 43 44 45
##46 47 48 49 50 51 52 53 54
##55 56 57 58 59 60 61 62 63
##64 65 66 67 68 69 70 71 72
##73 74 75 76 77 78 79 80 81



#To find certian x and y
class myTable():



        
    def __init__(self):
        self.board = []
        for i in range(1,82):
            cell = myCell()
            cell.setRow(((i-1)//9)+1)
            cell.setCol(i-((cell.getRow()-1)*9))
            #cell.setBox(((((cell.getRow()-1)//3)+1)*3)-(3-(((cell.getCol()-1)//3)+1)))
            self.board.append(cell)
        self.fill(self.board)

##    def getPos(self,x,y):
##        #returns List at x and y of list table
##        cell =getPos(table[(x+(9*(y-1)))])
##        return cell
        
    def fill(self,board):
        for cell in board:
            cell.pos= []
            if cell.getAnswer() == 0:
                for value in range(1,10):
                    if self.check(cell,value,board) == True:
                        cell.add(value)

    def check(self,cell,value,board):
        for checkCell in board:
            if (checkCell.getRow() == cell.getRow() or checkCell.getCol == cell.getCol() ) and value == checkCell.getAnswer():
                return False
            else:
                return True
    
    def single(self):
        done = True
        for cell in self:
            if len(cell.getPos) == 1:
                done = False
                cell.setAnswer(str(cell.getPos[0]))
                cell.removeCheck(cell,cell.getAnswer())
        return done
        
    def removeCheck(self,cell,value):
        for checkCell in self:
            if (checkCell.getRow() == cell.getRow() or checkCell.getCol == cell.getCol() or checkCell.getBox() == cell.getBox) and value in checkCell.getPos():
                checkCell - value

    def setCell(self, row, col, value):
            for i in range(0,81):
                if self.board[i].getRow() == row and self.board[i].getCol() == col:
                    self.board[i].setAnswer(value)
                    self.fill(self.board)

    def sortMinPos(self):
        self.sort(len(pos))
        return self
