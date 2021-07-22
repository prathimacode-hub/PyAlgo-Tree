# Python Program to demonstrate creation of Array using array creations
import array as arr

# creating an array with integer type
n = arr.array('i', [1, 2, 3,4])

# printing array
print("The new integer array is : ", end=" ")
for i in range(4):
    print(n[i], end =", ")
print()

# creating an array with float type
m = arr.array('d', [1.1, 1.5, 2.0])

# printing  array
print("The new Floating point array is : ", end=" ")
for i in range(3):
    print(m[i], end=", ")

print()

# Adding Elements to a Array using insert() and append() methods

# Creating an integer array
print("Array before insertion : ", end=" ")
for i in range(4):
    print(n[i], end=", ")
print()

# inserting array using insert()
n.insert(4, 5)

print("Array after insertion using insert(): ", end=" ")
for i in (n):
    print(i, end=", ")
print()

n.append(6)

print("Array after insertion using append(): ", end=" ")
for i in (n):
    print(i, end=", ")
print()

# printing initial array
print("The array is : ", end="")
for i in range(5):
    print(n[i], end=", ")

print("\r")

# using pop() to remove element
print("The popped element is : ", end="")
# Removing element at 4th position
print(n.pop(4))

# printing array
print("The array after popping is : ", end="")
for i in range(4):
    print(n[i], end=", ")

print("\r")

# using remove()
# removing the element at position 2
n.remove(2)

# printing array after removing
print("The array after removing is : ", end="")
for i in range(3):
    print(n[i], end=", ")






