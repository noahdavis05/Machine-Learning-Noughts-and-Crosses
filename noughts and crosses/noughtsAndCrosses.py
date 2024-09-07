class Grid:
    def __init__(self):
        self.grid = [[' ' for i in range(3)] for j in range(3)]
        

    def getGrid(self):
        return self.grid
    
    def getGridStringPrint(self):
        gridString = ''
        for row in self.grid:
            gridString += ' | '.join(row) + '\n'
        return gridString
    
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