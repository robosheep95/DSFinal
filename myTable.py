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
            cell.setBox(((((cell.getRow()-1)//3)+1)*3)-(3-(((cell.getCol()-1)//3)+1)))
            self.board.append(cell)
        ##self.fill(self.board)

##    def getPos(self,x,y):
##        #returns List at x and y of list table
##        cell =getPos(table[(x+(9*(y-1)))])
##        return cell
        
    def fill(self,board):
        for cell in board:
            if cell.getAnswer() == 0:
                for value in range(1,10):
                    if self.check(cell.getRow(),cell.getCol(),cell.getBox(),value,board):
                        cell.addPos(value)

    def check(self,row,col,box,value,board):
        for cell in board:
            #print("{},{},{},{}".format(checkCell.getRow(),checkCell.getCol(),checkCell.getBox(),value))
            #print("{},{},{}".format(cell.getRow(),cell.getCol(),cell.getBox()))
            if row == cell.getRow() and value == cell.getAnswer():
                return False
            elif col == cell.getCol() and value == cell.getAnswer():
                return False
            elif box == cell.getBox() and value == cell.getAnswer():
                return False
                        
        else:
            return True

        
    def single(self,board):
        done = False
        while not done:
            done = True
            for cell in board:
                if len(cell.getPos()) == 1:
                    done = False
                    cell.setAnswer(cell.getPos()[0])
                    self.removeCheck(cell.getRow(),cell.getCol(),cell.getBox(),cell.getAnswer(),board)
        
    def removeCheck(self,row,col,box,value,board):
        for cell in board:
            if row == cell.getRow() and value in cell.getPos():
                cell.removePos(value)
            elif col == cell.getCol() and value in cell.getPos():
                cell.removePos(value)
            elif box == cell.getBox() and value in cell.getPos():
                cell.removePos(value)

    def setCell(self, row, col, value):
            for i in range(1,82):
                if self.board[i].getRow() == row and self.board[i].getCol() == col:
                    self.board[i].setAnswer(value)
                    self.removeCheck(i,value)

    def sortMinPos(self,board):
        board.sort(key = lambda cell: cell.getLen())
        return board

##main
t = myTable()
t.board[0].setAnswer(0)
t.board[1].setAnswer(3)
t.board[2].setAnswer(1)
t.board[3].setAnswer(0)
t.board[4].setAnswer(0)
t.board[5].setAnswer(8)
t.board[6].setAnswer(0)
t.board[7].setAnswer(0)
t.board[8].setAnswer(0)
t.board[9].setAnswer(5)
t.board[10].setAnswer(0)
t.board[11].setAnswer(0)
t.board[12].setAnswer(0)
t.board[13].setAnswer(0)
t.board[14].setAnswer(0)
t.board[15].setAnswer(0)
t.board[16].setAnswer(0)
t.board[17].setAnswer(8)
t.board[18].setAnswer(0)
t.board[19].setAnswer(4)
t.board[20].setAnswer(2)
t.board[21].setAnswer(0)
t.board[22].setAnswer(5)
t.board[23].setAnswer(0)
t.board[24].setAnswer(0)
t.board[25].setAnswer(0)
t.board[26].setAnswer(6)
t.board[27].setAnswer(0)
t.board[28].setAnswer(0)
t.board[29].setAnswer(8)
t.board[30].setAnswer(0)
t.board[31].setAnswer(1)
t.board[32].setAnswer(0)
t.board[33].setAnswer(0)
t.board[34].setAnswer(9)
t.board[35].setAnswer(0)
t.board[36].setAnswer(1)
t.board[37].setAnswer(0)
t.board[38].setAnswer(4)
t.board[39].setAnswer(7)
t.board[40].setAnswer(2)
t.board[41].setAnswer(0)
t.board[42].setAnswer(3)
t.board[43].setAnswer(0)
t.board[44].setAnswer(5)
t.board[45].setAnswer(0)
t.board[46].setAnswer(6)
t.board[47].setAnswer(0)
t.board[48].setAnswer(0)
t.board[49].setAnswer(4)
t.board[50].setAnswer(0)
t.board[51].setAnswer(2)
t.board[52].setAnswer(0)
t.board[53].setAnswer(0)
t.board[54].setAnswer(2)
t.board[55].setAnswer(0)
t.board[56].setAnswer(0)
t.board[57].setAnswer(0)
t.board[58].setAnswer(8)
t.board[59].setAnswer(0)
t.board[60].setAnswer(7)
t.board[61].setAnswer(5)
t.board[62].setAnswer(0)
t.board[63].setAnswer(6)
t.board[64].setAnswer(0)
t.board[65].setAnswer(0)
t.board[66].setAnswer(0)
t.board[67].setAnswer(0)
t.board[68].setAnswer(0)
t.board[69].setAnswer(0)
t.board[70].setAnswer(0)
t.board[71].setAnswer(9)
t.board[72].setAnswer(0)
t.board[73].setAnswer(0)
t.board[74].setAnswer(0)
t.board[75].setAnswer(9)
t.board[76].setAnswer(0)
t.board[77].setAnswer(0)
t.board[78].setAnswer(1)
t.board[79].setAnswer(2)
t.board[80].setAnswer(0)
t.fill(t.board)
for cell in t.board:
    print (cell.getPos())
t.single(t.board)
print()
for cell in t.board:
    print (cell.getPos())
t.sortMinPos(t.board)
print()
for cell in t.board:
    print (cell.getPos())
