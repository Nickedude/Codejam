def nextMove(P):
    i = len(P) - 1                              # Start at the top
    while(i > 0):                               # Loop until i == 1
        if(P[i-1] == 'C') and (P[i] == 'S'):    # Look at the two adjecent letters. If they're CS, swap them.
            return i                            # Return index to swap
        i = i - 1

    return -1                                   # If no such pair could be found, return -1


# Checks if the total damage is <= D
def isSolved(D, P):
    strength = 1                                # The initial strength of the beam is 1
    damage = 0                                  # Initially we haven't taken any damage
    for i in range(0,len(P)):                   # Loop through the whole list of instructions
        if(P[i] == 'S'):                        # If the instruction is S we're taking damage
            damage = damage + strength
        elif(P[i] == 'C'):                      # If the instruction is C the strength increases
            strength = strength * 2
        else:
            print("Something is wrong!")

    if(damage <= D):                            # If total damage <= D we're OK
        return True
    else:                                       # Otherwise we're not
        return False

# Swaps to elements in a list
def swap(theList, i, j):
    tmp = theList[i]
    theList[i] = theList[j]
    theList[j] = tmp

# Solves the problem
def solve(pair):
    (D,P) = pair            # Unbox pair
    P = list(P)
    #print(P)
    D = int(D)              # Convery to int
    solved = isSolved(D,P)  # Check if it's solved
    moves = 0               # Counts the number of moves made

    while (not solved):         # While it isn't solved, make a change
        i = nextMove(P)         # Get the next move
        if(i < 0):              # If no move can be made we stop
            break

        swap(P,i,i-1)           # Perform the move
        moves = moves + 1       # Increment moves
        solved = isSolved(D,P)  # Check if it's solved
        #print(P)

    return (solved,moves)       # Return the solution



T = int(input())     # Read nr of cases
cases = []

for i in range(0,T):
    D, P = input().split(" ")
    cases.append((D,P))

for i in range(0, len(cases)):
    (result, number) = solve(cases[i])
    base = "Case #" + str(i+1) + ": "
    if(result):
        print(base + str(number))
    else:
        print(base + "IMPOSSIBLE")
