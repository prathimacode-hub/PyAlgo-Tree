# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W
 
# Problem Statement : Returns the maximum value that 
#                     can be put in a knapsack of
#                     capacity W
 
# Author : Abhishek Sharma, 2021

# -----------------------------------------------------------------

# Solution for the above problem statement using Python 3 language.
# Approach : Dynamic Method

# -----------------------------------------------------------------    
 
# This is the main function which will provide us maximum value that
# can be put in the capacity of W
 
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 
 
# Driver code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print ("- 0-1 Knapsack Problem using Dynamic Method - ")
print ("-----------------------------------------------------")
print ()
print ("The values given : ")
print (val)
print ("-----------------------------------------------------")
print ("The corresponding weights are :")
print (wt)
print ("-----------------------------------------------------")
print ("The maximum capacity can be : ")
print (W)
print ()
print ("-----------------------------------------------------")
print ("Output :\nMaximum total value of the Knapsack : ")
print (knapSack(W, wt, val, n))

# -----------------------------------------------------------------   
# Input given :
# The values given : 
# [60, 100, 120]
# -----------------------------------------------------
# The corresponding weights are :
# [10, 20, 30]
# -----------------------------------------------------
# The maximum capacity can be : 
# 50

# -----------------------------------------------------
# Output :
# Maximum total value of the Knapsack : 
# 220

# -----------------------------------------------------------------   

# Code contributed by, Abhishek Sharma, 2021
