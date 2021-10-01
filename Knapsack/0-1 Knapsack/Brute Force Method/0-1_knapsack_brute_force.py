# A naive recursive implementation
# of 0-1 Knapsack Problem
# Brute Force Method
 
# Problem Statement : Returns the maximum value that 
#                     can be put in a knapsack of
#                     capacity W
 
# Author : Abhishek Sharma, 2021

# -----------------------------------------------------------------

# Solution for the above problem statement using Python 3 language.
# Approach : Brute Force Method

# -----------------------------------------------------------------    
 
# This is the main function which will provide us maximum value that
# can be put in the capacity of W

def knapSack(W, wt, val, n):
 
    # Base Case
    if n == 0 or W == 0:
        return 0
 
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
 

# end of function knapSack
 
 
#Driver Code
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print ("- 0-1 Knapsack Problem using Brute Force Method - ")
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
