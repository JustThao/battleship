from random import randint

# constants
# use xLength and yLength for number of columns/rows
# xLength = int(input('how many columns?: '))
# yLength = int(input('how many rows?: '))
xLength = 9
yLength = 9
shipSize = randint(1,4)
direction = randint(1,2)
xPos = 0
yPos = 0

# 1 == horizontal, 2 == vertical
if (direction == 1 and xLength >= shipSize):
    xPos = randint(1, xLength - shipSize + 1)
elif (direction == 2 and yLength >= yPos):
    yPos = randint(1, yLength - shipSize + 1)
else:
    print('couldnt be placed because not enough space')

def printBoard(board):
    for i in range(yLength + 1):
        if i > 0:
            print(i, end = " ") #column outline
            for j in range(1, xLength + 1):
                print(board[(i, j)], end = " ")
        else:
            for j in range(xLength + 1):
                print(j, end = " ") #row outline

        print()

def boardArr():
    row = {}
    for i in range(yLength + 1):
        for j in range(1, xLength + 1):
            row[i,j] = 0                
    return row

def createShips():
    pass

# TODO gets x y coordinates from user input 
def guess():
    # newBoard = boardArr()
    # yPos input
    # xPos input
    # newBoard[y,x] = 1
    # print the board
    pass
    
    
def game():
    printBoard(boardArr())
    guess()


printBoard(boardArr())