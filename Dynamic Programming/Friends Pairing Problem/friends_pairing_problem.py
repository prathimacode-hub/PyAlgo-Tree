# Problem Statement : Given n friends, each one can 
#                     remain single or can be paired up
#                     with some other friend. Each friend
#                     can be paired only once. Find out the
#                     total number of ways in which friends
#                     can remain single or can be paired up.

# -----------------------------------------------------------------

# Method : Dynamic Programming
# Abhishek Sharma. 2021

# -----------------------------------------------------------------

# Python program solution of friends pairing problem
 
# Returns count of ways n people can remain single or paired up.

# -----------------------------------------------------------------

# This is the main function which provides the number of ways
# friends can e single.

def countFriendsPairings(n):
 
    dp = [0 for i in range(n + 1)]
 
    # Filling dp[] in bottom-up manner using
    # recursive formula explained above.
    
    for i in range(n + 1):
 
        if(i <= 2):
            dp[i] = i
        else:
            dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]
 
    return dp[n]
 
# Driver code

print ("- Friends Pairing Problem using Dynamic Programming - ")
print ("------------------------------------------------------")
n = int(input("Enter the number : "))
print ("------------------------------------------------------")
print ()
print ("Output :")
print("Number of ways people can remain single or, paired up : ",countFriendsPairings(n))


# -----------------------------------------------------------------   
# Input given :
# - Friends Pairing Problem using Dynamic Programming - 
# ------------------------------------------------------
# Enter the number : 3
# ------------------------------------------------------

# Output :
# Number of ways people can remain single or, paired up :  4

# ------------------------------------------------------

# Code contributed by, Abhishek Sharma, 2021
