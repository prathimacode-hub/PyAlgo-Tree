# Problem Name: Nth Catalan Numbers
# Approach: Dynamic Programming

# -----------------------------------------------------------------------------------

# Problem Statement: Catalan numbers are defined as a mathematical sequence 
#                    that consists of positive integers, which can be used to 
#                    find the number of possibilities of various combinations. 
#                    Find out the catalan numbers in between the range from 0 to N.


# -----------------------------------------------------------------------------------

# Constraints:
# n -> Integer taken as the range of the Catalan Numbers.
# catalan[] -> Array of Catalan Numbers from 0 to n.

# -----------------------------------------------------------------------------------

# A dynamic programming based function to find nth
# Catalan number
 
def catalan(n):
    if (n == 0 or n == 1):
        return 1
 
    # Table to store results of subproblems
    catalan = [0]*(n+1)
 
    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1
 
    # Fill entries in catalan[]
    # using recursive formula
    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
 
    # Return last entry
    return catalan[n]
 
 
# Driver Code
print ("-- Nth Catalan Numbers using Dynamic Programming --")
print ()
print ("Enter the upper range : ")
k = int(input())
print ()
print ("Printing Nth Catalan Numbers from 0 to {0}...".format(k))
print ()
print ("Here you go!")
for i in range(k):
	  print(catalan(i), end=" ")
    
    
# -----------------------------------------------------------------------------------

# Output:
# -- Nth Catalan Numbers using Dynamic Programming --

# Enter the upper range : 
# 12

# Printing Nth Catalan Numbers from 0 to 12...

# Here you go!
# 1 1 2 5 14 42 132 429 1430 4862 16796 58786 

# -----------------------------------------------------------------------------------

# Code Contributed by, Abhishek Sharma, 2022

# -----------------------------------------------------------------------------------
