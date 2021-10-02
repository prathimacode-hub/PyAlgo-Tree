# A Python program to find n'th Bell number
# Approach : Dynamic Programming
# Abhishek S, 2021

# ----------------------------------------------------------

# Problem statement : Given a set of n elements, find the 
#                     number of ways of partitioning it.

# ----------------------------------------------------------

# Solution : Used the Dynamic Approach to solve the problem.

# This is the working function which will check and return the
# nth bell numbers one after another using the Dynamic Programming
# method

def bellNumber(n):
 
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
 
        # Explicitly fill for j = 0
        bell[i][0] = bell[i-1][i-1]
 
        # Fill for remaining values of j
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
 
    return bell[n][0]
 
# Driver program
print ("- Bell Numbers using Dynamic Programming Approach -")
print ("---------------------------------------------------")
print ()
z = int(input("Enter the number of numbers you wanna print : "))
print ()
print ("---------------------------------------------------")
print ()
print ("Output : ")
print ()
for n in range(z):
    print('Bell Number', n, 'is', bellNumber(n))
    
    

# ----------------------------------------------------------

# Enter the number of numbers you wanna print : 6

# ----------------------------------------------------------

# Output : 

# Bell Number 0 is 1
# Bell Number 1 is 1
# Bell Number 2 is 2
# Bell Number 3 is 5
# Bell Number 4 is 15
# Bell Number 5 is 52

# ----------------------------------------------------------

# Code contributed by, Abhishek Sharma, 2021
