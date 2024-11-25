import random
def start_game():

    # declaring an empty list then appending 4 list each with four elements as 0.
    mat =[]
    for i in range(4):
        mat.append([0] * 4)

    # controls for user
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")

    # calling the function to add a new 2 in grid after every step
    add_new_2(mat)
    return mat

# function to add a new 2 in grid at any random empty cell
def add_new_2(mat):

   # choosing a random index for row and column.
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    # while loop will break as the
    # random cell chosen will be empty
    # (or contains zero)
    while(mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    # we will place a 2 at that empty random cell.
    mat[r][c] = 2
    
# function to get the current state of game
def get_current_state(mat):

    # if any cell contains
    # 2048 we have won
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 2048):
                return 'WON'

    # if we are still left with atleast one empty cell game is not yet over
    for i in range(4):
        for j in range(4):
            if(mat[i][j]== 0):
                return 'GAME NOT OVER'

    # or if no cell is empty now
    # but if after any move left, right,
    # up or down, if any two cells
    # gets merged and create an empty
    # cell then also game is not yet over
    for i in range(3):
        for j in range(3):
            if(mat[i][j]== mat[i + 1][j] or mat[i][j]== mat[i][j + 1]):
                return 'GAME NOT OVER'

    for j in range(3):
        if(mat[3][j]== mat[3][j + 1]):
            return 'GAME NOT OVER'

    for i in range(3):
        if(mat[i][3]== mat[i + 1][3]):
            return 'GAME NOT OVER'

    # else lost
    return 'LOST'


