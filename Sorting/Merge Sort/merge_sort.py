# function for merge sort
def merge_sort(arr):
    if len(arr) > 1:

        # mid element of array
        mid = len(arr) // 2

        # Dividing the array and calling merge sort on array
        left = arr[:mid]

        # into 2 halves
        right = arr[mid:]

        # merge sort for array first
        merge_sort(left)

        # merge sort for array second
        merge_sort(right)

        # merging function
        merge_array(arr, left, right)


def merge_array(arr, left, right):
    i = j = k = 0

    # merging two array left right in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # merging any remaining element
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# printing array
def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


total_element = int(input("Number of element in array "))
arr = []
for i in range(total_element):
    arr.append(int(input(f"Enter {i}th element ")))
print("Input array is ", end="\n")
print_array(arr)

merge_sort(arr)
print("array after sort is: ", end="\n")
print_array(arr)

