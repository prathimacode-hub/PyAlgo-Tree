# Radix Sort Algorithm
🔴 Language used : **Python 3**

## 🎯 Aim
The aim of this script is to perform the sorting process using the Radix Sort algortihm.

## 👉 Purpose
The main purpose of this script is to show the implementation of Radix Sort algorithm on an unsorted array of elements to make it a sorted one, with less time complexity than the merge sort, quick sort.

## 📄 Description
Radix sort is the linear sorting algorithm that is used for integers. In Radix sort, there is digit by digit sorting is performed that is started from the least significant digit to the most significant digit.

The process of radix sort works similar to the sorting of students names, according to the alphabetical order. In this case, there are 26 radix formed due to the 26 alphabets in English. In the first pass, the names of students are grouped according to the ascending order of the first letter of their names. After that, in the second pass, their names are grouped according to the ascending order of the second letter of their name. And the process continues until we find the sorted list.

🔴 Examples: 

```
Constraints: 
arr[] -> array of unsorted elements.
countingSort(arr, exp1) -> implementation of Counting Sort before Radix Sort.
radixSort(arr) -> implementation of Radix sort.

Input:
Array before implementing the Radix Sort...
170 45 75 90 802 24 2 66

Radix Sort going on...

Output:
After implementing Radix Sort algorithm...
2 24 45 66 75 90 170 802
```

## 📊 Flowchart
```
radixSort(arr)  
max = largest element in the given array  
d = number of digits in the largest element (or, max)  
Now, create d buckets of size 0 - 9  
for i -> 0 to d  
sort the array elements using counting sort (or any stable sort) according to the digits at  
the ith place  
```

## 🧮 Algorithm
The steps used in the sorting of radix sort are listed as follows -
- First, we have to find the largest element (suppose max) from the given array. Suppose `x` be the number of digits in max. The `x` is calculated because we need to go through the significant places of all elements.
- After that, go through one by one each significant place. Here, we have to use any stable sorting algorithm to sort the digits of each significant place.
Now let's see the working of radix sort in detail by using an example. 

To understand it more clearly, let's take an unsorted array and try to sort it using radix sort. It will make the explanation clearer and easier.

For the understanding of the algorithm let's take the above mentioned example,
The Input array is given as, 
```
[170, 45, 75, 90, 802, 24, 2, 66]
```

## 💻 Input and Output 
- **Test Case 1 :**
```
Input Given :
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
```

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Greedy/Activity%20Selection%20Problem/Images/asp-1.png)

- **Test Case 2 :**
```
Input Given :
s = [1, 2, 3, 4, 7, 8, 9, 9, 11, 12]
f = [3, 5, 4, 7, 10, 9, 11, 13, 12, 14]
```
![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Greedy/Activity%20Selection%20Problem/Images/asp-2.png)

## ⏰ Time and Space complexity
- **Time Complexity :** `O(n)`.
- **Space Complexity :** `O(1)`.

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2022 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
