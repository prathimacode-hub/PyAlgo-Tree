# Problem Name: Radix Sort Algorithm
# Problem Statement: Given an unsorted array of elements (here integers),
#                    the task is to perform the Radix Sort algorithm to
#                    sort the elements in the ascending order.

# ------------------------------------------------------------------------------

# Constraints: 
# arr[] -> array of unsorted elements.
# countingSort(arr, exp1) -> implementation of Counting Sort before Radix Sort.
# radixSort(arr) -> implementation of Radix sort.

# ------------------------------------------------------------------------------

# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.
 
def countingSort(arr, exp1):
 
    n = len(arr)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
# Method to do Radix Sort
def radixSort(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10
 
 
# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66]

print ("-- Implementation of Radix Sort Algorithm --")
print ()
print ("Array before implementing the Radix Sort...")
print (" ".join(str(k) for k in arr))
print ()
print ("Radix Sort going on...")
print ()
print ("After implementing Radix Sort algorithm...")
 
# Function Call
radixSort(arr)
print (" ".join(str(k) for k in arr)) 

# ------------------------------------------------------------------------------

# Output:
# -- Implementation of Radix Sort Algorithm --

# Array before implementing the Radix Sort...
# 170 45 75 90 802 24 2 66

# Radix Sort going on...

# After implementing Radix Sort algorithm...
# 2 24 45 66 75 90 170 802

# ------------------------------------------------------------------------------

# Code contributed by, Abhishek Sharma, 2022

# ------------------------------------------------------------------------------
