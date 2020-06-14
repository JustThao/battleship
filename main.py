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

def printBoard(boardArr):
    # print the board
    # todo nhat
    # hallo
    pass

def board():
    # returns the current state of the board
    pass

# gets x y coordinates from user input and prints the board after
def guess():
    # newBoard = board
    # xPos input
    # yPos input
    # newBoard[y][x] = 1
    # print the board
    pass
    
    
def game():
    pass

