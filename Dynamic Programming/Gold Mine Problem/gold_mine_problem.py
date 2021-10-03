# Python program to solve
# Gold Mine problem

# Problem Statement : Returns maximum amount of
#                     gold that can be collected
#                     when journey started from
#                     first column and moves
#                     allowed are right, right-up
#                     and right-down
 
# ----------------------------------------------------------------- 

# Approach : Brute Force Method
# Abhishek S, 2021

# ----------------------------------------------------------------- 

MAX = 100
 

def getMaxGold(gold, m, n):
 
    # Create a table for storing
    # intermediate results
    # and initialize all cells to 0.
    # The first row of
    # goldMineTable gives the
    # maximum gold that the miner
    # can collect when starts that row
    goldTable = [[0 for i in range(n)]
                        for j in range(m)]
 
    for col in range(n-1, -1, -1):
        for row in range(m):
 
            # Gold collected on going to
            # the cell on the rigth(->)
            if (col == n-1):
                right = 0
            else:
                right = goldTable[row][col+1]
 
            # Gold collected on going to
            # the cell to right up (/)
            if (row == 0 or col == n-1):
                right_up = 0
            else:
                right_up = goldTable[row-1][col+1]
 
            # Gold collected on going to
            # the cell to right down (\)
            if (row == m-1 or col == n-1):
                right_down = 0
            else:
                right_down = goldTable[row+1][col+1]
 
            # Max gold collected from taking
            # either of the above 3 paths
            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down)
                                                            
    # The max amount of gold
    # collected will be the max
    # value in first column of all rows
    res = goldTable[0][0]
    for i in range(1, m):
        res = max(res, goldTable[i][0])
 
    return res
     
# Driver code
gold = [[1, 3, 3],
    [2, 1, 4],
    [0, 6, 4]]
 
m = 3
n = 3
print ("- Gold Mine Problem using Dynamic Programming -")
print ("-----------------------------------------------")
print ()
print ("Output : ")
print ("The maximum amount of Gold can be collected : ")
print(getMaxGold(gold, m, n))


# -------------------------------------------------------------------------

# Output
# - Gold Mine Problem using Dynamic Programming -
# -----------------------------------------------

# Output : 
# The maximum amount of Gold can be collected : 
# 12

# -------------------------------------------------------------------------

# Code contributed by, Abhishek S, 2021
