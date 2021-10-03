import numpy as np
## VECTOR AND ARRAY OPERATIONS
# Creating 3x4 Matrix 
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
# Create vector of 5 elements
B = np.array([5,6,8,9,7])
print(B)
# Multiplication of Array
o = np.array([2,3,4,5])
o*2
print(o)
# Random array creation
C = np.random.randint(10, size=(3,3))
print(C.shape)
print(C.size)
print(C)
# Dot Product of Matrix
d = np.array([9,8,0])
e = np.array([6,6,6])
print(np.dot(d,e))
# Addition and Subtraction of Matrix
i = np.array([1,2,3])
k = np.array([1,2,3])
print("i + k is {}".format(i + k))
print("i - k is {}".format(i - k))
# Identity Matrix
I3 = np.identity(3, dtype = int)
print(I3)
# Transpose of Matrix
print(e)
print(e.T)



