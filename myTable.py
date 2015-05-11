"""
Sudoku Solver
Taylor Scafe, Jordan Huddleston
May 11, 2015
"""

##01 02 03 04 05 06 07 08 09
##10 11 12 13 14 15 16 17 18
##19 20 21 22 23 24 25 26 27
##28 29 30 31 32 33 34 35 36
##37 38 39 40 41 42 43 44 45
##46 47 48 49 50 51 52 53 54
##55 56 57 58 59 60 61 62 63
##64 65 66 67 68 69 70 71 72
##73 74 75 76 77 78 79 80 81

from myCell import *

class myTable():

    def __init__(self,newdata):
        """Create table with row, column, and box. Takes input and fills in answers."""
        self.board = []
        for i in range(1,82):
            cell = myCell()
            cell.setRow(((i-1)//9)+1)
            cell.setCol(i-((cell.getRow()-1)*9))
            cell.setBox(((((cell.getRow()-1)//3)+1)*3)-(3-(((cell.getCol()-1)//3)+1)))
            self.board.append(cell)
        #newdata = input("Space seperated list, use 0 for unknown\n").split()
        count = 0
        newdata = newdata.split()
        for cell in self.board:
            cell.setAnswer(int(newdata[count]))
            count +=1
        
    def fill(self,board):
        """Takes input value in range, places in table"""
        for cell in board:
            if cell.getAnswer() == 0:
                for value in range(1,10):
                    if self.check(cell.getRow(),cell.getCol(),cell.getBox(),value,board):
                        cell.addPos(value)
                        
    def check(self,row,col,box,value,board):
        """Used by fill, checks if value is a valid possibility."""
        for cell in board:
            #print("{},{},{}".format(cell.getRow(),cell.getCol(),cell.getBox()))
            if row == cell.getRow() and value == cell.getAnswer():
                return False
            elif col == cell.getCol() and value == cell.getAnswer():
                return False
            elif box == cell.getBox() and value == cell.getAnswer():
                return False          
        else:
            return True

        
    def simple(self,board):
        """Checks all cells for single possibilities, then calls removeCheck."""
        done = False
        while not done:
            done = True
            for cell in board:
                if len(cell.getPos()) == 1:
                    done = False
                    cell.setAnswer(cell.getPos()[0])
                    self.removeCheck(cell.getRow(),cell.getCol(),cell.getBox(),cell.getAnswer(),board)
        if done:
            if self.isBad(board):
                pass
                
        
    def removeCheck(self,row,col,box,value,board):
        """Removes possibilities in other cells after new possibility inked in"""
        for cell in board:
            if row == cell.getRow() and value in cell.getPos():
                cell.removePos(value)
            elif col == cell.getCol() and value in cell.getPos():
                cell.removePos(value)
            elif box == cell.getBox() and value in cell.getPos():
                cell.removePos(value)

    def sortMinPos(self,board):
        board.sort(key = lambda cell: cell.getLen())
        return board

    
    def guess(self,board):
        """Breaks cells that have two possibilites into two seperate tables. Then solves."""
        self.sortMinPos(self.board)
        output1 = board[:]
        output2 = board[:]
        for cell in output1:
            if cell.getLen()>0:
                print(cell.getPos())
                cell.setPos(cell.getPos()[0])   
        for cell in output2:
            if cell.getLen()>0:
                print(cell.getPos())
                cell.setPos(cell.getPos()[1])
        return(output1,output2)
        
    def isBad(self,board):
        """If cell in table returns no answer and no possibilities, returns True."""
        for cell in board:
            if cell.getAnswer() == 0 and cell.getLen() == 0:
                return True
        return False


    def isFinished(self,board):
        """If every cell has valid answer, returns True"""
        for cell in board:
            if cell.getAnswer() == 0:
                return False
        return True

####main
    
string1 = "0 0 2 1 8 0 0 6 5 0 7 0 9 0 0 8 0 0 6 3 0 0 0 2 0 0 1 5 0 0 6 2 0 7 0 0 7 9 0 0 0 0 0 4 2 0 0 4 0 1 9 0 0 8 8 0 0 2 0 0 0 9 3 0 0 6 0 0 5 0 8 0 4 2 0 0 7 3 1 0 0"
string2 = "0 2 0 0 9 0 0 6 0 9 0 3 0 0 0 4 0 1 0 0 1 4 0 3 7 0 0 3 0 0 7 0 6 0 0 5 0 0 0 2 0 9 0 0 0 8 0 0 5 0 1 0 0 2 0 0 9 8 0 4 1 0 0 6 0 5 0 0 0 9 0 8 0 4 0 0 1 0 0 3 0"
string3 = "0 0 0 8 0 0 0 0 2 5 0 0 7 0 0 8 0 9 0 0 2 0 0 0 0 0 6 1 0 0 0 5 0 2 9 0 0 0 0 4 0 8 0 0 0 0 4 3 0 9 0 0 0 1 3 0 0 0 0 0 9 0 0 9 0 6 0 0 1 0 0 8 8 0 0 0 0 6 0 0 0"

t = myTable(string3)
t.fill(t.board)
for cell in t.board:
    print(cell.getPos())
print()
t.simple(t.board)
for cell in t.board:
   print(cell.getPos())

