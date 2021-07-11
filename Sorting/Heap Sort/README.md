## Heap Sort

### Algorithm
1. Build a max heap from the input data. 
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of the tree. 
3. Repeat step 2 while the size of the heap is greater than 1.

### Language Used : Python

### The overall time complexity of Heap Sort is O(nLogn).

### Sample Testcases

**Input**                         
5 4 3 2 1  
**Output**  
1 2 3 4 5

**Input**  
31 4 12 4  
**Output**  
4 4 12 31

### Output & Input
![](https://github.com/thejaswin123/PyAlgo-Tree/blob/main/Sorting/Heap%20Sort/Images/heap_sort.png)

### Author

[Thejaswin S](https://github.com/thejaswin123)
