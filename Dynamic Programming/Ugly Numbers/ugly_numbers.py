# Python program to find n'th Ugly number
# Method : Dynamic Programming
# Abhishek Sharma. 2021

# Problem Statement : Ugly numbers are numbers whose 
#                     only prime factors are 2, 3 or 5.
#                     Find out the nth Ugly number, where n is
#                     given as the input to the program.

# -----------------------------------------------------------------    

# Function to get the nth ugly number 
 
def getNthUglyNo(n):
 
    ugly = [0] * n  # To store ugly numbers
 
    # 1 is the first ugly number
    ugly[0] = 1
 
    # i2, i3, i5 will indicate indices for
    # 2,3,5 respectively
    i2 = i3 = i5 = 0
 
    # Set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
 
    # Start loop to find value from
    # ugly[1] to ugly[n]
    for l in range(1, n):
 
        # Shoose the min value of all
        # available multiples
        ugly[l] = min(next_multiple_of_2,
                      next_multiple_of_3,
                      next_multiple_of_5)
 
        # Increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
 
        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
 
        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
 
    # Return ugly[n] value
    return ugly[-1]
 
# Driver Code
if __name__ == '__main__':
    print ("- Finding out n'th Ugly Number using Dynamic Method -")
    print ("-----------------------------------------------------")
    n = int(input("Enter any number : "))
    print ()
    print ("********************************************")
    print ("The desired Ugly number is : ",getNthUglyNo(n))
    
    
    
# -----------------------------------------------------------------   
# Input given :
# - Finding out n'th Ugly Number using Dynamic Method -
# -----------------------------------------------------
# Enter any number : 150

# -----------------------------------------------------
# Output :
# The desired Ugly number is :  5832

# -----------------------------------------------------------------   

# Code contributed by, Abhishek Sharma, 2021
