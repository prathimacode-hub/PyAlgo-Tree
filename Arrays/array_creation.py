# Python Program to demonstrate creation of Array using array creations
import array as arr

# creating an array with integer type
n = arr.array('i', [1, 2, 3])

# printing array
print("The new integer array is : ", end=" ")
for i in range(3):
    print(n[i], end =", ")
print()

# creating an array with float type
m = arr.array('d', [1.1, 1.5, 2.0])

# printing  array
print("The new Floating point array is : ", end=" ")
for i in range(3):
    print(m[i], end=", ")