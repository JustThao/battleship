from random import randint

xLength = 9
yLength = 9

# 1 == horizontal, 2 == vertical
# if (direction == 1 and xLength >= shipSize):
#     xPos = randint(1, xLength - shipSize + 1)
# elif (direction == 2 and yLength >= yPos):
#     yPos = randint(1, yLength - shipSize + 1)
# else:
#     print('couldnt be placed because not enough space')

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
    for i in range(1, yLength + 1):
        for j in range(1, xLength + 1):
            row[i,j] = 0                
    return row

# TODO fix bug, ships has wrong output
def createShips():
    ships = []
    buffer = {}
    shipCount = 3
    for i in range(shipCount):
        shipSize = randint(1,4)
        startPosition = randint(1, xLength)
        for j in range(shipSize):
            buffer[startPosition, j] = 0
        ships.append(buffer)
    return ships

def guess():
    while True:
        try:
            newBoard = boardArr()
            yy = int(input("y-coordinate: "))
            xx= int(input("x-coordinate: "))
            pair = str(input("(" + str(yy) + "," + str(xx) + ") right? Y/N\n"))
            if pair == "Y" or pair == "y":
                break
        except ValueError:
                       print()
                
    #if newBoard[(yy, xx)] == ship: #need value for ship
        #newBoard[(yy, xx)] = 1
    #else:
        #newBoard[(yy, xx)] = "x"
    
    #print(newBoard)
    
    
def game():
    printBoard(boardArr())
    guess()

print(createShips())