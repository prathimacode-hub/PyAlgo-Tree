# Program to implement QuickSort Algorithm in Python

'''
This function takes last element as pivot, places  the pivot element at
its correct position in sorted  array, and places all smaller(smaller than
pivot) to left of pivot and all greater elements to right  of pivot
'''

def partition(arr, low, high):
    '''
    The value of i is initialized to (low-1) since initially first element
    is swapped by itself
    Reason: no greater element has been encountered apart from itself
    '''
    pivotElement = arr[high]
    i = (low - 1)

    for j in range(low, high):
        if arr[j] < pivotElement:
            i += 1
            # swap elements arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # swap pivot element with element at index=(i + 1) since loop ended,
    # to obtain LHS of pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return(i + 1)

'''
This is the calling function that implements QuickSort algorithm, where:
arr = input array given by user
low = starting index
high = ending index
'''

def quickSort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# main function
if __name__ == "__main__":
    print('Enter the number of elements: ')
    n = int(input())
    print('Enter the elements of the array: ')
    arr = list(map(int, input().split()))
    quickSort(arr, 0, n-1)

    # print the final sorted array in ASCending order
    print('The sorted array is: ')
    for i in range(n):
        print(arr[i], end=" ")
    print()

'''
Input :
Enter the number of elements: 5
Enter the elements of the array: 22 11 44 55 33

Output :
The sorted array is: 11 22 33 44 55

Time & Space Complexity
Best or average case Time Complexity: O(nlogn)
Worst case Time Complexity: O(n^2)
Space Complexity: O(logn)
'''