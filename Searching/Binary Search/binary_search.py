def binary_search(arr, x):
    start= 0
    end = len(arr) - 1
    mid = 0
    while start<= end:
        mid = (start+ end) // 2
        # If x is greater, search in right array
        if arr[mid] < x:
            start = mid + 1

        # If x is smaller, search in left array
        elif arr[mid] > x:
            end= mid - 1
        # if x is present at mid
        else:
            return mid
 

    # when we reach at the end of array, then the element was not present
    return -1
 

arr = [ ]
n=int(input("Enter size of array : "))
print("Enter array  elements : ")
for i in range(n):
    e=int(input())
    arr.append(e)
x = int(input("Enter element to search "))
ans = binary_search(arr, x)
if(ans==-1):
    print("Element not found")
else:
    print("Element found at ",ans)