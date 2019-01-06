import sys

def smallColumnDone(row, col):
    for i in range(row-1,row+2):
        if(world[i][col-1] == 0):
            return False

    return True

def lowerRowDone(row, col):
    for i in range(col-1,col+2):
        if(world[row-1][i] == 0):
            return False

    return True

def columnDone(col):
    for i in range(topRow,botRow+1):
        if(world[i][col] == 0):
            return False

    return True


def getNextMove(row, col, direction):
    if(direction == 'right'):                       # If we're moving right
        if(smallColumnDone(row, col)):               # If the three cells in the column to the left are done, move along
            if(col < rightCol-1):                   # If we aren't at the rightmost column, move to the right
                if(columnDone(col)):                # If a complete column is done, shrink the area to be processed
                    leftCol = leftCol + 1
                return(row, col+1, direction)       # Move to the right by incrementing column
            else:                                   # If we're at the last column
                direction = 'up'                    # Change direction to up

        else:                                       # If the left column isn't done, try to complete it
            return(row, col, direction)

    if(direction == 'up'):                          # If we're moving up
        if(lowerRowDone(row,col)):                  # If the lower row is done, move
            if(row > topRow-1):                     # If we're not at the top, move upwards
                if(rowDone(row)):                   # If the former row is complete, shrink area to be processed
                    botRow = botRow - 1
                return(row+1, col, direction)
            else:                                   # If we're at the top, move to the leftCol
                direction = 'left'

        else:                                       # If the lower row isn't done, try to complete it
            return(row, col, direction)

    if(direction == 'left'):
        if(smallColumnDone(row, col)):               # If the three cells in the column to the left are done, move along
            if(col < rightCol-1):                   # If we aren't at the rightmost column, move to the right
                if(columnDone(col)):                # If a complete column is done, shrink the area to be processed
                    leftCol = leftCol + 1
                return(row, col+1, direction)       # Move to the right by incrementing column
            else:                                   # If we're at the last column
                direction = 'up'                    # Change direction to up

        else:                                       # If the left column isn't done, try to complete it
            return(row, col, direction)

    if(direction == 'down')




def printDoubleList(list):
    for i in range(0, len(list)):
        print(list[i])




T = int(input())     # Read the number of test cases
size = 10
failed = False

for i in range(0,T):
    if(failed):         # Stop processing cases if we've failed
        break

    A = int(input())            # Read the minimum area
    if((A%4)!=0):               # If A is not divisible by four ...
        A = A + (4 - (A%4))     # ... make it divisible by four!
    width = int(A/4)            # Calculate width
    height = 4                  # Calculate height

    while(width > size):        # Refit if it doesn't fit
        if(width%2==1):
            width = width + 1
        width = width/2
        height = height * 2

    center = 5
    direction = 'right'
    leftCol = int(center - (width/2))
    topRow = int(center - (height/2))
    rightCol = leftCol + width - 1
    botRow = topRow + height - 1
    currCol = leftCol + 1
    currRow = botRow - 1

    world = [[0 for j in range(0,size)] for k in range(0,size)]
    count = 0

    while(count < 1000):
        count = count + 1
        (currRow, currCol, direction) = getNextMove(currRow, currCol, direction)
        print(str(currRow) + " " + str(currCol))
        sys.stdout.flush()
        ansRow, ansCol = [int(s) for s in input().split(" ")]

        if(ansRow == ansCol == 0):              # Done
            break

        if(ansRow == ansCol == -1):             # Something went wrong :-)
            failed = True
            break

        world[ansRow][ansCol] = 1
        printDoubleList(world)


'''
    print("Height: " + str(height))
    print("Width: " +str(width))
    print("Leftcol: " + str(leftCol))
    print("Toprow: " + str(topRow))
    print("RightCol: " + str(rightCol))
    print("Botrow: " + str(botRow))
    print("Currol" + str(currCol))
    print("Currrow" + str(currRow))
'''
