import numpy as np
from random import randint
#
# GENERATES A RANDOM GRID BASED ON PROBABILIY OF CHOICE, CAN USE TO GENERATE NEGATIVE EXAMPLES FOR SUPERVISED TRAINING
# 
def create_rand_grid(prob, SIZE):
    grid = np.random.choice(a=[False, True], size=(SIZE, SIZE), p=[prob, 1-prob])  
    return grid
    #(','.join(str(col) for row in grid for col in row))

def flip(x):
    if x == 0:
        return 1
    else:
        return 0

def create_pos_grid(grid):
    rows = len(grid)
    cols = rows
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 1:
                x = randint(1,5)
                #x = randint(1,6)
                if   x == 1:
                    grid[i][j-1] = flip(grid[i][j-1])
                elif x == 2:
                    grid[i+1][j] = flip(grid[i+1][j])
                elif x == 3:
                    grid[i][j+1] = flip(grid[i][j+1])
                elif x == 4: 
                    grid[i - 1][j] = flip(grid[i - 1][j])
    return grid