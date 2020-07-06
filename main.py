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
#def createShips():
    #ships = []
    #buffer = {}
    #shipCount = 3
    #for i in range(shipCount):
        #shipSize = randint(1,4)
        #startPosition = randint(1, xLength)
        #for j in range(shipSize):
            #buffer[startPosition, j] = 0
        #ships.append(buffer)
    #return ships

# TODO fix double value

def createShips():
    
    buffer = {}
    shipCount = 3
    #1 == horizontal, 2 == vertical
    
    for i in range(shipCount):
        
        #while True:
            
         #   try:
          #      direction = int(input("For placing ship horizontal enter '1' and vertical enter '2'. " + "Ship " + str(i+1) + ": "))
           #     shipSize = randint(1,4) #maybe shipsize = randint(1, int(xLength/2) or randint(1, int(yLength/2)))
            #    if direction == 1 or direction == 2:
             #       break
              #  else:
               #     print("Please enter either 1 or 2")
            #except ValueError:
             #   print("Please enter either 1 or 2")
                
        if i == 0:
            shipSize = 3
        elif i == 1:
            shipSize = 2
        elif i == 2:
            shipSize = 1
        direction = 1
        
        if (direction == 1 and xLength >= shipSize): #placing ship horizontal
            start_position_y = randint(1, xLength - shipSize + 1)
            start_position_x = randint(1, xLength - shipSize + 1)
            
            while start_position_x + shipSize > xLength:
                start_position_x = randint(1, xLength - shipSize + 1) #avoiding outside the box
            j = 0
            buff = {}
            
            while j < shipSize:
                if not (start_position_y, start_position_x + j + 1) in buffer:
                    buff[start_position_y, start_position_x + j + 1] = 0
                    j += 1
                else:
                    buff = {}
                    j = 0
                    start_position_y = randint(1, xLength - shipSize + 1)
            for k in buff:
                    buffer[k] = 0
                            
        elif (direction == 2 and yLength >= shipSize):  #placing ship vertical   
            start_position_y = randint(1, yLength - shipSize + 1)
            start_position_x = randint(1, yLength - shipSize + 1)
            
            while start_position_y + shipSize > yLength:
                start_position_y = randint(1, yLength - shipSize + 1) #avoiding outside the box
            j = 0
            buff = {}
            
            while j < shipSize:
                if not (start_position_y + j + 1, start_position_x) in buffer:
                    buff[start_position_y + j + 1, start_position_x] = 0
                    j += 1
                else:
                    buff = {}
                    j = 0
                    start_position_x = randint(1, yLength - shipSize + 1)
            for k in buff:
                    buffer[k] = 0
    
    return buffer


def guess():
    newBoard = boardArr()
    ships = createShips()
    #print(ships) for testing purpose
    while True:
        try:
            # TODO compare KEYS! (yy,xx) with ships
            yy = int(input("y-coordinate: "))
            xx = int(input("x-coordinate: "))
            break
            
        except ValueError:
            print()

        
    if (yy, xx) in ships:
        newBoard[(yy, xx)] = 1
    else:
        newBoard[(yy, xx)] = "x"
    #print(newBoard)
    return newBoard
    
    
def game():
    printBoard(boardArr())
    guess()

game()