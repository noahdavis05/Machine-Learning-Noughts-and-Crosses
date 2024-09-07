from noughtsAndCrosses import Grid
from bot import Bot
import pygame

"""
The class where the game is played.
Where the player plays against the bot, taking it in turns with who goes first.
"""
class Game:

    # pygame window is initiated and the grid drawn on screen.
    def __init__(self):
        pygame.init()
        self.width = 600
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        # create the grid and store the Rect objects in a list
        self.gridRects = []
        for i in range(3):
            for j in range(3):
                self.gridRects.append(pygame.Rect(j * 200, i * 200, 200, 200))
        
        

    def newRound(self,char):
        self.player1 = Bot(char)
        self.grid = Grid()
    
    def playRounds(self):
        roundCount = 0
        botFirst = 0
        self.botWins = 0
        self.playerWins = 0
        self.draws = 0
        while roundCount < 1000:
            roundCount += 1
            if roundCount % 2 == 0:
                char = "X"
                playerChar = "O"
                botFirst = 0
            else:
                char = "O"
                playerChar = "X"
                botFirst = 1
            self.newRound(char)
            
            gameOver = False
            moveCount = 0
            while not gameOver:
                if moveCount % 2 == botFirst:
                    # bot should make a move
                    self.player1.checkBoard(self.grid)
                    row,col = self.player1.makeMove()
                    if self.grid.getGridPosition(row,col) == " ":
                        self.grid.setGrid(row, col, self.player1.char)
                        moveCount += 1
                    else:
                        print("something has gone wrong")
                    
                    
                else:
                    # check player input to make a move
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = pygame.mouse.get_pos()
                            for i, rect in enumerate(self.gridRects):
                                if rect.collidepoint(mouse_pos):
                                    row = i // 3
                                    col = i % 3
                                    if self.grid.getGridPosition(row,col) == " ":
                                        self.grid.setGrid(row, col, playerChar)
                                        moveCount += 1
                                    break

                # check the winner, if there is one
                if not self.grid.checkWin():
                    if moveCount == 9:
                        print('Draw')
                        self.draws += 1
                        gameOver = True
                        self.printStats()
                        

                else:
                    gameOver = True
                    print(self.grid.getGridStringPrint())
                    #print(self.grid.checkWin())
                    # work out if the bot or player won the game
                    if botFirst % 2 == 0:
                        if self.grid.checkWin() == "X":
                            print("The bot won")
                            self.botWins += 1
                        else:
                            print("The player won")
                            self.playerWins += 1
                    else:
                        if self.grid.checkWin() == "X":
                            self.playerWins += 1
                            print("The player won")
                        else:
                            self.botWins += 1
                            print("The bot won")

                    self.printStats()
                

                self.updateScreen()
            

    def updateScreen(self):  
        self.window.fill((255, 255, 255))  # fill the window with white color
        for i, rect in enumerate(self.gridRects):
            pygame.draw.rect(self.window, (0, 0, 0), rect, 2)  # draw the grid rectangles
            row = i // 3
            col = i % 3
            if self.grid.getGrid()[row][col] == "X":
                pygame.draw.line(self.window, (0, 0, 0), rect.topleft, rect.bottomright, 2)  # draw X
                pygame.draw.line(self.window, (0, 0, 0), rect.bottomleft, rect.topright, 2)  # draw X
            elif self.grid.getGrid()[row][col] == "O":
                pygame.draw.circle(self.window, (0, 0, 0), rect.center, 100, 2)  # draw O
        pygame.display.update()  # update the display

    def printStats(self):
        print("Player wins", self.playerWins)
        print("Bot wins", self.botWins)
        print("Draws", self.draws)


# game initiated and played.
game = Game()

game.playRounds()




