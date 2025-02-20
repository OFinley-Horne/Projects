from random import *

class Cell():
    '''cell of the maze'''
    ## the cells of the maze
    def __init__(self, x, y):
        self.pos = x + y * 3
        self.x = x
        self.y = y  
        self.visted = False


class Maze():
    '''randomly creates a maze pathway'''
    def __init__(self):

        self.grid = 3
        self.cells = []
        self.stack = []
  
    def create_cells(self):
        '''creates the cells for the map'''
        #gets the columns of the grid
        for cols in range(self.grid):
            #gets the rows of the grid
            for rows in range(self.grid):
                #puts the row and column into a cell
                c = Cell(rows, cols)
                #add that to the cell list
                self.cells.append(c)
    
    # so I can visualize this stuff           
    grid = [[(0,0), (1,0), (2,0), (3,0), (4,0)],
            [(0,1), (1,1), (2,1), (3,1), (4,1)],
            [(0,2), (1,2), (2.2), (3,2), (4,2)],
            [(0,3), (1,3), (2,3), (3,3), (4,3)],
            [(0,4), (1,4), (2,4), (3,4), (4,4)]]
    grid = [[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24]]
    
    def check_cell(self, x, y):
        '''checks if a cell is outside the boundaries of the grid'''
        if x < 0 or x > self.grid -1 or y < 0 or y >  self.grid -1: #checks if x is less than the grid then checks if it is greater then the same for y
            return False
        else:
            return True
            
    def check_neighbours(self, pos):
        '''checks the neighbouring cells puts them in a list and randomly chooses 
        one to add to the stack. Then removes from stack when no neighbours'''

        #makes the cell visted
        self.cells[pos].visted = True
        #make neighbour list
        neighbours = []
        #to chose a random number
        ranlis = []
        
       # this gets the cells x(rows), and ys(columns) to the left, right, down, and up then puts it into the equation x + y * columns which gives you the position of a cell in a 1d list

        #left
        leftx, lefty = self.cells[pos].x -1, self.cells[pos].y
        #position of the left cell
        leftpos = leftx + lefty * self.grid
       
        #right
        rightx, righty = self.cells[pos].x + 1, self.cells[pos].y
        rightpos = rightx + righty* self.grid
        # down
        downx, downy = self.cells[pos].x, self.cells[pos].y + 1
        downpos = downx + downy * self.grid
        #up
        upx, upy = self.cells[pos].x, self.cells[pos].y - 1 
        uppos = upx + upy * self.grid
        
        #takes the position of a cell verifies that you can go to it and checks if you have gone to that cell before
        
        #left
        if self.check_cell(leftx, lefty) and self.cells[leftpos].visted == False:
            #if you havent add the cell to the neighbour list
            neighbours.append(leftpos)
        #right
        if self.check_cell(rightx, righty) and self.cells[rightpos].visted == False:
            neighbours.append(rightpos)
        #down
        if self.check_cell(downx, downy) and self.cells[downpos].visted == False:
            neighbours.append(downpos)
        #up
        if self.check_cell(upx, upy) and self.cells[uppos].visted == False:
            neighbours.append(uppos)
        
        #checks if there are no numbers in neighbour list
        if not neighbours:
                
                journey = []
                #get the journey you took to get to this cell
                for i in self.stack:
                    journey.append(i.pos)
                #print the journey
                print(journey)
                #remove the last item in list
                self.stack.pop()
                #if no items in stack then you are done
                if not self.stack:
                    print('finished')
                else:
                    #recurese the last item in stack if there are items in stack and none in neighbours
                    self.check_neighbours(self.stack[-1].pos)
        else:
            #grab all neighbouring cells and put them in a list
            for i in neighbours:
                ranlis.append(i)
            #randomly chose one
            rannum = choice(ranlis)
            #put it in the stack
            self.stack.append(self.cells[rannum])
            #recurse the new one you just put in the stack
            self.check_neighbours(self.stack[-1].pos)


m = Maze()
m.create_cells()
m.check_neighbours(0)
