from random import randint

# constants
# use xLength and yLength for number of columns/rows
# xLength = int(input('how many columns?: '))
# yLength = int(input('how many rows?: '))
xLength = 10
yLength = 10
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

# TODO make this function generic by using a board parameter instead of row
# TODO use xLength and yLength constants instead of static numbers (10)
def printBoard():
    row = {}
    for i in range(0, 10):
        if i > 0:
            print(i, end = " ") #column outline
            for j in range(1, 10):
                row[i,j] = 0
                print(row[(i,j)], end = " ")    
        else:
            for j in range(0, 10):
                print(j, end = " ") #row outline
        print()

# TODO generate the row dictionary which can be used as argument for printBoard()
def boardArr():
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
    printBoard()
    guess()

game()