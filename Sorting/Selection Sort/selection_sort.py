def selectionSort(array, n):
   
    for i in range(n):
        minimum = i

        for j in range(i + 1, n):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[j] < array[minimum]:
                minimum = j
         
        # put min at the correct position
        (array[i], array[minimum]) = (array[minimum], array[i])


data = [ ]
size = int(input("Enter size of array : "))
print("Enter array elements: ")
for i in range(size):
     e=int(input())
     data.append(e)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)