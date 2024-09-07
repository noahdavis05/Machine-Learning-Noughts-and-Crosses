"""
Class for the noughts and crosses grid.
"""
class Grid:
    def __init__(self):
        self.grid = [[' ' for i in range(3)] for j in range(3)]
        

    def getGrid(self):
        return self.grid
    
    # returns a noughts and crosses grid with the current items in the grid in a form to be displayed in the command line.
    def getGridStringPrint(self):
        gridString = ''
        for row in self.grid:
            gridString += ' | '.join(row) + '\n'
        return gridString
    
    # returns the string of the grid
    def getGridString(self):
        gridString = ''
        for i in self.grid:
            for j in i:
                gridString += j

        return gridString
    
    def getGridPosition(self, row, col):
        return self.grid[row][col]
    
    def setGrid(self, row, col, value):
        self.grid[row][col] = value

    
    # function checks if any player has won the round.
    # returns the winner, and if no one has won it returns false.
    def checkWin(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] and self.grid[i][0] != ' ':
                return self.grid[i][0]
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] and self.grid[0][i] != ' ':
                return self.grid[0][i]
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != ' ':
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != ' ':
            return self.grid[0][2]
        return False