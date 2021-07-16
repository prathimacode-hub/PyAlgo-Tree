''' This program illustrates the shell sort implementation in Python

 Shell sort or Shell's method, is an in-place comparison sort.
 It can be seen as either a generalization of sorting by exchange (bubble sort) or sorting by
 insertion (insertion sort). The method starts by sorting pairs of elements far apart from each other,
 then progressively reducing the gap between elements to be compared. Starting with far apart elements
 can move some out-of-place elements into position faster than a simple nearest neighbor exchange.

  Best Case O(n logn); Average Case O(depends on gap sequence); Worst Case O(n^2)'''



def shell_sort(arr):                          #function for shell sort
    sublistCount = int(len(arr)/2)            

    while sublistCount > 0:
        for start in range(sublistCount):
            do_insertsort_gap(arr,start,sublistCount)
        sublistCount = int(sublistCount/2)    
    return arr    

def do_insertsort_gap(arr,start,gap):
    for i in range(start+gap,len(arr),gap):
        currentValue = arr[i]
        position = i
        while position >= gap and arr[position-gap] >= currentValue:
            arr[position] = arr[position-gap]                             # We compare values in each sub-list and swap them (if necessary) in the original array.
            position = position-gap
        arr[position] = currentValue        

array = input("Enter the elements of the array separated by space : ")    #Taking input
array = [int(x) for x in array.split(" ")]                                #string to int conversion

print(f"Array after sorting is : {shell_sort(array)}")                    #printing the output


# sample Test case    
""" >>> shell_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> shell_sort([])
    []
    >>> shell_sort([-2, -5, -45])
    [-45, -5, -2]
    """
