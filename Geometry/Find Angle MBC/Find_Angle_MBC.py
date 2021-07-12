# Geometry Problem : Find the ∠MBC from the given figure

# Category : Geometry
# Challenge taken from HackerRank
# Language used : Python 3.7
# Difficulty as per HackerRank : Medium



'''
Problem Statement : ABC is a right triangle with 90° at B
                    Therefore ∠ABC = 90°
                    Point M is the midpoint of hypotenuse .
                    You are given the lengths AB and BC.
                    Your task is to find ∠MBC (angle θ°, as shown 
                    in the figure) in degrees.
'''


# Importing required package
# here we are using math package

import math


# Taking the required inputs
# Here we have to take the lengths of the sides AB and BC

# 1. Enter the length of AB

print ('Enter the value of AB : ')
ab = float(input())

# 2. Enter the length of BC

print ('Enter the value of BC : ')
bc = float(input())

# Finding out the length of the hypotenuse
# Here the hypotenuse is AC

ac = math.sqrt((ab*ab)+(bc*bc))

# As the hypotenuse is divided into to equal parts by MB
# Finding out the length of BM

bm = ac / 2.0

# As MC = BM

mc = bm

# Now take all those required values in dummy parameters for further usage
#let,

b = mc
c = bm
a = bc

# As the hypotenuse is divided into two parts MC = BM
# where b=c

# Using cosine to find out the value of the angle angle B
# But the angle will be in the radian unit

angel_b_radian = math.acos(a / (2*b))

# Change the angle in degree unit using the pi function

angel_b_degree = int(round((180 * angel_b_radian) / math.pi))

# Creating the final output and adding the degree symbol 
# Final Output

output_str = str(angel_b_degree)+'°'


# Printing the final output 

print ('----------------------------------')
print('∠MBC = ',output_str)


'''
---------------------------------------------------------------------------------

Test Case #1

User Input :
Enter the value of AB : 
35
Enter the value of BC : 
45

---------------------------------------------------------------------------------

Output :
∠MBC =  38°

---------------------------------------------------------------------------------

Test Case #2

User Input
Enter the value of AB : 
10
Enter the value of BC : 
10

---------------------------------------------------------------------------------

Output :
∠MBC =  45°

---------------------------------------------------------------------------------

'''


# --------------------------------------------------------------------------------
# This codebase will solve the problem named, 'Find angle MBC'
# All the explanations are done in the README.md folder with proper visualization

# Hope this problem will find you interesting enough
# Author : Abhishek Sharma, DCP21
