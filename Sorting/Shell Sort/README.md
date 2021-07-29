
### Script Name
Shell Sort

### Aim
To write a program for Shell Sort

### Purpose
To get a understanding about the algorithm of Shell Sort

### Short description of package/script
Shell sort is a highly efficient sorting algorithm and is based on insertion sort algorithm. Shell sort is the generalization of insertion sort which overcomes the drawbacks of insertion sort by comparing elements separated by a gap of several positions.

### Workflow of the Project
* Divide the array in the form of N/2 (where N is the length of array).
* Compare the elements and swap like 0th element with 4th,1st and 5th and so on.
* Now again divide the array in the form of N/4 (where N is the length of array).
* Compare the elements and swap.
* Continue the steps of dividing till the elements are compared with interval of 1.

### Detailed explanation of script, if needed
Shell sort divides the array in the form of N/2 , N/4 , …, 1 (where N is the length of array) and then sorting is done. This breaking of sequence and sorting takes place until the entire array is sorted.

Let's take an example to understand.

12	15	50	10	35	19	11	44
**Stage 1: Divide**
In this stage the unsorted array is divided in the form of N/2. Here N/2 is 8/2 = 4, which means the 0th and 4th elements, 1st and 5th and so on are compared and swapped if necessary.

Now after first stage the array is in this form:

12	15	11	10	35	19	50	44
**Stage 2: Again Divide**
In this stage the unsorted array is again divided in the form of N/4. Here N/4 is 8/4 = 2, which means the 0th and 2th elements, 1st and 3th and so on are compared and swapped if necessary.

Now after second stage the array is in this form:

11	10	12	15	35	19	50	44
**Stage 3: Again Divide when the interval 1**
In this stage the unsorted array is again divided in the form of N/8. Here N/8 is 8/8 = 1, which means the 0th and 1th elements, 1st and 2th and so on are compared and swapped if necessary.

Now after final stage the array is in this form:

10	11	12	15	19	35	44	50
After the final process the unsorted array is sorted.

### Sample Test Case
Enter size: 6
Enter elements:
5
4
3
2
1
0

Sorted Array:
0
1
2
3
4
5

### Setup instructions
Just clone the repository .

### Output
<img src="https://github.com/prathimacode-hub/PyAlgo-Tree/blob/3e08153a796610d5cc7579c352d74c9993e47bc3/Sorting/Shell%20Sort/Images/Output1.png">

<img src="https://github.com/prathimacode-hub/PyAlgo-Tree/blob/e1bff3b00ee020a088bf942a98a90b311f53484a/Sorting/Shell%20Sort/Images/Output2.png"

### Author(s)
Neha Jha

