# Adding Elements to a Array using insert() and append() methods

# importing array creations
import array as arr

# Creating an integer array
n = arr.array('i', [1, 2, 3, 4])

print("Array before insertion : ", end=" ")
for i in range(4):
    print(n[i], end=", ")
print()

# inserting array using insert()
n.insert(4, 5)

print("Array after insertion : ", end=" ")
for i in (n):
    print(i, end=", ")
print()

# array with float type
m = arr.array('d', [2,0, 1.1, 4.51])

print("Array before insertion : ", end=" ")
for j in range(3):
    print(m[j], end=", ")
print()

# adding an element using append()
m.append(1.1)

print("Array after insertion : ", end=" ")
for i in (m):
    print(i, end=", ")
print()