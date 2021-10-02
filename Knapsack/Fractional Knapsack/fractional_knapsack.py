# Python3 program to solve fractional
# Knapsack Problem
  
# Problem Statement : Given weights and values of n items, 
#                     we need to put these items in a 
#                     knapsack of capacity W to get the 
#                     maximum total value in the knapsack.

# ----------------------------------------------------------------- 

# Approach : Brute Force Method
# Abhishek S, 2021

# ----------------------------------------------------------------- 

# Solution : Using the Brute Force method we can figure out the solution


# This function returns the item values of the data class
class ItemValue:
  
    """Item Value DataClass"""
  
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt
  
    def __lt__(self, other):
        return self.cost < other.cost
  
# Greedy Approach
  
# this function is the main architecture to solve the program.  
class FractionalKnapSack:
  
    """Time Complexity O(n log n)"""
    def getMaxValue(wt, val, capacity):
        """function to get maximum value """
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))
  
        # sorting items by value
        iVal.sort(reverse=True)
  
        totalValue = 0
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity -= curWt
                totalValue += curVal
            else:
                fraction = capacity / curWt
                totalValue += curVal * fraction
                capacity = int(capacity - (curWt * fraction))
                break
        return totalValue
  
  
# Driver Code
if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50
    print ("- Fractional Knapsack Problem using Brute Force Method - ")
    print ("-----------------------------------------------------")
    print ()
    print ("The values given : ")
    print (val)
    print ("-----------------------------------------------------")
    print ("The corresponding weights are :")
    print (wt)
    print ("-----------------------------------------------------")
    print ("The maximum capacity can be : ")
    print (capacity)
    print ()
    print ("-----------------------------------------------------")
    print ()
    print ("Output : ")
    # Function call
    maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)

    
# -----------------------------------------------------------------   
# Input given :
# The values given : 
# [60, 40, 100, 120]
# -----------------------------------------------------
# The corresponding weights are :
# [10, 40, 20, 30]
# -----------------------------------------------------
# The maximum capacity can be : 
# 50

# -----------------------------------------------------
# Output :
# Maximum total value of the Knapsack : 
# 240.0

# -----------------------------------------------------------------   

# Code contributed by, Abhishek Sharma, 2021
