# Problem Name: Activity Selection Problem
# Method used: Greedy Approach

# -------------------------------------------------------------------------

# Problem Statement: You are given n activities with their start and finish times. 
#                    Select the maximum number of activities that can be performed 
#                    by a single person, assuming that a person can only work on a 
#                    single activity at a time. 

# -------------------------------------------------------------------------

# Constraints:
# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities


# Let's solve the problem.

# This is the actual function, which is going to find out the result for this problem.
# The function printMaxActivities takes two parameters, s and f
# s[] denotes all the start time activities.
# f[] denotes all the finish time activities.
def printMaxActivities(s, f ):
    n = len(f)
    print ("The following activities are selected")
 
    # The first activity is always selected
    i = 0
    print (i,end=' ')
 
    # Consider rest of the activities
    for j in range(1, n):
 
        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            print (j,end=' ')
            i = j
 
# Driver program to test above function
print ("-- Activity Selection Problem using Greedy Approach --\n")
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
print ("** Activities during start time **")
print (s)
print ("** Activities during finish time **")
print (f)
print ()
printMaxActivities(s , f)


# -------------------------------------------------------------------------

# Output:
# -- Activity Selection Problem using Greedy Approach --

# ** Activities during start time **
# [1, 3, 0, 5, 8, 5]
# ** Activities during finish time **
# [2, 4, 6, 7, 9, 9]

# The following activities are selected
# 0 1 3 4 

# -------------------------------------------------------------------------

# Code contributed by, Abhishek Sharma, 2022

# -------------------------------------------------------------------------
