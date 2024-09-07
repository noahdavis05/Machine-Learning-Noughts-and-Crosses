from noughtsAndCrosses import Grid
import sqlite3
import random

class Bot:
    def __init__(self, character):
        self.char = character
        self.conn = sqlite3.connect('training.db')
        self.c = self.conn.cursor()
        self.log = []

    def readBoard(self, board):
        self.board = board.getGridString()

    def checkBoard(self,b):
        self.board = b.getGridString()
        # check database to see if this board has previously been there
        statement = "SELECT * FROM game_data WHERE board = '" + self.board + "'"
        self.c.execute(statement)
        result = self.c.fetchone()
        if result:
            #print(" Board already exists in database")
            pass
        else:
            # create a new record for this board in traing.db
            #print("Board does not exist in database")
            tempList = []
            for i in range(0,9):
                if self.board[i] == " ":
                    tempList.append(10)
                else:
                    tempList.append(0)
            statement = 'INSERT INTO game_data (board, pos0, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            self.c.execute(statement, (self.board, tempList[0], tempList[1], tempList[2], tempList[3], tempList[4], tempList[5], tempList[6], tempList[7], tempList[8]))
            self.conn.commit()
            print("New board added to database")

        # bot should make a move

    def makeMove(self):
        # board must be in db already as should either be there or just added in 
        statement = "SELECT * FROM game_data WHERE board = '" + self.board + "'"
        self.c.execute(statement)
        result = self.c.fetchone()
        # now i must get the results of pos0 - pos8
        tempList = []
        for i in range(2,11):
            tempList.append(result[i])

        total = sum(tempList)
        newTempList = []
        for num in tempList:
            newTempList.append(num/total)

        randNum = random.random()
        tempNum = 0
        for i in range(0,9):
            tempNum += newTempList[i]
            if tempNum > randNum:
                move = i
                break
        
        self.logMove(move)

        row = move // 3
        col = move % 3

        '''movesList = []
        for i in range(0,9):
            for j in range(0,tempList[i]):
                movesList.append(i)

        move = random.choice(movesList)
        self.logMove(move)
        row = move // 3
        col = move % 3'''
        return row, col
    
    def logMove(self, move):
        temp = [ self.board, move ]
        self.log.append(temp)

    def endRound(self, Movebonus):
        #check who won
        print(self.log , self.char)
        # go through the log and updates the correct moves with the bonus
        for move in self.log:
            statement1 = "SELECT pos" + str(move[1]) + " FROM game_data WHERE board = '" + move[0] + "'"
            print(statement1)
            self.c.execute(statement1)
            result = self.c.fetchone()
            score = result[0]
            if score <= 1:
                score = 5

            statement2 = "UPDATE game_data SET " + "pos" + str(move[1]) + " = " + str(score + Movebonus) + " WHERE board = '" + move[0] + "'"
            print(statement2)
            self.c.execute(statement2)
        self.conn.commit()
        self.conn.close()

    
    