def shell_sort(arr):
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
            arr[position] = arr[position-gap]
            position = position-gap
        arr[position] = currentValue        

array = input("Enter the elements of the array separated by space : ")
array = [int(x) for x in array.split(" ")]

print(f"Array after sorting is : {shell_sort(array)}")      
