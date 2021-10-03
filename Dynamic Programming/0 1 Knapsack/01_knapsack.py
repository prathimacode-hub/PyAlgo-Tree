# This is the memoization approach of 0 / 1 Knapsack in Python in simple
# Method : Dynamic Programming
# Author : Neeraj Pratap Hazarika

# Problem Statement : Given a set of items, each with a weight and a value, take items to include in a knapsack such that the total weight is less than or equal to a given limit and the total value is as large as possible. Print the total value.

# ------------------------------------------------------------

# declare universal scope 2d matrix, dp
dp=[[]]
 
def knapsack(wt, val, W, n):
 
    # base conditions
    if n == 0 or W == 0:
        return 0
    if dp[n][W] != -1:
        return dp[n][W]
 
    # choice diagram code
    if wt[n-1] <= W:
        dp[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
        return dp[n][W]
    elif wt[n-1] > W:
        dp[n][W] = knapsack(wt, val, W, n-1)
        return dp[n][W]

# Driver code
if __name__ == '__main__':
    # Inputs
    W = int(input("Enter the maximum weight the knapsack can hold : "))
    n = int(input("Enter number of items to be choosen from : "))
    print("Enter the weights to be choosen from : ")
    wt = list(map(int,input().strip().split()))[:n]
    print("Enter the values corresponding to these weights : ")
    val = list(map(int,input().strip().split()))[:n]

    # Initialize 2d matrix, dp 
    dp = [[-1 for i in range(W + 1)] for j in range(n + 1)]

    print("Maximum profit : ",knapsack(wt, val, W, n))

# ------------------------------------------------------------

# Inputs given :
# Enter the maximum weight the knapsack can hold : 50
# Enter number of items to be choosen from : 3
# Enter the weights to be choosen from : 
# 10 20 30 
# Enter the values corresponding to these weights : 
# 60 100 120

# Output :
# Maximum profit : 220