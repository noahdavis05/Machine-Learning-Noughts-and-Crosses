from noughtsAndCrosses import Grid
from bot import Bot


for i in range(0,1000000):
    print(i)

    myGrid = Grid()
    myBot1 = Bot("X")
    myBot2 = Bot("O")


    gameOver = False
    moveCount = 0

    while not gameOver:
        print(myGrid.getGridStringPrint())
        if moveCount % 2 == 0:
            myBot1.checkBoard(myGrid)
            row, col = myBot1.makeMove()
            myGrid.setGrid(row, col, "X")
        else:
            myBot2.checkBoard(myGrid)
            row, col = myBot2.makeMove()
            myGrid.setGrid(row, col, "O")

        moveCount += 1




        if not myGrid.checkWin():
            if moveCount == 9:
                print('Draw')
                gameOver = True
                # reward both bots for a draw
                myBot1.endRound(1)
                myBot2.endRound(1)
                
        else:
            print(myGrid.getGridStringPrint())
            print(myGrid.checkWin() + ' wins')
            gameOver = True
            if myGrid.checkWin() == "X":
                # reward bot1 for winning and punish bot2 for losing
                myBot1.endRound(5)
                myBot2.endRound(-1)
            else:
                # reward bot2 for winning and punish bot1 for losing
                myBot1.endRound(-1)
                myBot2.endRound(5)





    
    
