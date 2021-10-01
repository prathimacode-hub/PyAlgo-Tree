# Subset Sum Problem using Dynamic Programming
# Directory : Dynamic Programming
# Language used : Python 3
# Abhishek S, 2021

# ------------------------------------------------------------------

# Problem Statement : A Dynamic Programming solution for subset
#                     sum problem Returns true if there is a subset of
#                     set[] with sun equal to given sum

# ------------------------------------------------------------------

# Solution : Creating the Python script to find out the required output.


 
# Returns true if there is a subset of set[]
# with sum equal to given sum
def isSubsetSum(set, n, sum):
     
    # The value of subset[i][j] will be
    # true if there is a
    # subset of set[0..j-1] with sum equal to i
    subset =([[False for i in range(sum + 1)]
            for i in range(n + 1)])
     
    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = True
         
    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sum + 1):
         subset[0][i]= False
             
    # Fill the subset table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j<set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>= set[i-1]:
                subset[i][j] = (subset[i-1][j] or
                                subset[i - 1][j-set[i-1]])
     
    # uncomment this code to print table
    # for i in range(n + 1):
    # for j in range(sum + 1):
    # print (subset[i][j], end =" ")
    # print()
    return subset[n][sum]
         
# Driver code
if __name__=='__main__':
    print (" - Subset Sum Problem using Dynamic Programming - ")
    print ("--------------------------------------------------")
    print ()
    set = list(map(int, input("Enter the set of numbers : ").split(" ")))
    print ()
    sum = int(input("Enter the subset sum : "))
    print ()
    print ("--------------------------------------------------")
    print ()
    print ("Calculating the result...")
    print ()
    print ("The Output is : ")
    n = len(set)
    if (isSubsetSum(set, n, sum) == True):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")
        
        
# ------------------------------------------------------------------
# Input Cases :
# Enter the set of numbers : 1 5 3 7 4
# Enter the subset sum : 12

# ------------------------------------------------------------------
# Output :
# Calculating the result...

# The Output is : 
# Found a subset with given sum

# ------------------------------------------------------------------

# Code contributed by, Abhishek Sharma, 2021
