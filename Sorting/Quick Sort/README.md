### Script Name
Quick Sort

### Aim
To write a program for Quick Sort

### Purpose
To get a understanding about the algorithm of Quick Sort

### Short description of package/script
Quick Sort is a sorting algorithm that follows Divide and Conquer. In this algorithm, it picks an element as a pivot and arranges the array according to this pivot element. The condition to arrange the array according to pivot element is that all the elements which are smaller than or equal to pivot must lie on the left side of the pivot. And all the elements which are greater than the pivot must lie on the right side of the pivot. Quick sort is not an in-place algorithm but to make it in-place it requires additional amounts of the array.

### Workflow of the Project
In this algorithm firstly it picks a pivot element and arranges the array according to this pivot element. The condition to arrange the array according to pivot element is that all the elements which are smaller than or equal to pivot must lie on the left side of the pivot. And all the elements which are greater than the pivot must lie on the right side of the pivot. After that follow the same approach on the left part of the pivot and right part of the pivot respectively until we left with a single element and finally we got our array sorted.

### Detailed explanation of script, if needed
In Quick Sort, we follow the following algorithm:

First we have to pick a pivot element.

Partition the array according to the pivot element, where the smaller or equal elements compare to the pivot must lie on the left side and greater on the right side.

Apply the previous two steps on the left part of the pivot and the right part of the pivot respectively.

Apply the previous step until we left with a single element.

Let's consider an Array arr[]:

Array arr[4] : | 11 | 22 | 44 | 33 |   

Pivot element : 33 

After Partition : | 11 | 22  | 33 | 44 |   

Left Part : | 11 | 22 | 

Right part : | 44 |  

Pivot element : | 22 |

left part : | 11 |

Here is our sorted array: | 11 | 22 | 33 | 44 |


### Setup instructions
Just clone the repository .

### Output

<img src="https://github.com/prathimacode-hub/PyAlgo-Tree/blob/1f340543e6cee34c0851017ce4040486ea8ce7d8/Sorting/Quick%20Sort/Images/output1.png">

<img src="https://github.com/prathimacode-hub/PyAlgo-Tree/blob/7cd90dac93bcaa2d9514d6d1139e7816a24d9d41/Sorting/Quick%20Sort/Images/output2.png">

### Author(s)
Neha Jha
