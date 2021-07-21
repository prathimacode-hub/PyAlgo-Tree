# Removal of elements in a Array using remove(), pop()

# importing "array" for array operations
import array as arr

# initializing array with array values
a = arr.array('i', [1, 2, 3, 4, 5, 6])

# printing initial array
print("The array is : ", end="")
for i in range(5):
    print(a[i], end=", ")

print("\r")

# using pop() to remove element
print("The popped element is : ", end="")
# Removing element at 4th position
print(a.pop(4))

# printing array
print("The array after popping is : ", end="")
for i in range(4):
    print(a[i], end=", ")

print("\r")

# using remove()
# removing the element at position 2
a.remove(2)

# printing array after removing
print("The array after removing is : ", end="")
for i in range(3):
    print(a[i], end=", ")