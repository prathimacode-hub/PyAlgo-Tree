''' 
Aim: Read a complex number as input from user, complec_num and print 
its value in polar coordinates.

'''

#importing cmath library
import cmath

#getting the input
complex_num= complex(int(input("Enter your x value : ")),int(input("Enter your y value: ")))

#using library converting the complex values into coordinates
r = float(abs(complex_num))
theta = float(cmath.phase(complex_num))

#printing the output
print("Your inputed complex number is :",complex_num)
print("r : ",r)
print("theta :",theta)
print("Hence Polar co-ordinates are : {0:0.4f} + i{1:0.4f}".format(r,theta))


'''
sample input 1 :
x : 4 y : 3
sample output 1 :
r : 5.0 theta : 0.643

sample input 2 :
x : 1 y : 2
sample output 2 : 
r : 2.361 theta : 1.107

Explaination :
The user enters two values x and y , which stand for x+iy in complex 
number notation.This inputted values are then converted into r and theta 
using the abs function on x and phase function on y.

'''