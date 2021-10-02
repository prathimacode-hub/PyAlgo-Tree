# Bell Numbers Problem using Dynamic Programming
Language used : **Python 3**

## 🎯 Aim
The aim of this script is to find out the nth Bell numbers using Dynamic Programming method..

## 👉 Purpose
The main purpose of this script is to show the implementation of Dynamic Programming to find out nth Bell Numbers.

## 📄 Description
- **What is Bell Number ?** -- Let `S(n, k)` be total number of partitions of n elements into k sets. The value of n’th Bell Number is sum of `S(n, k)` for `k = 1 to n`. Value of `S(n, k)` can be defined recursively as, `S(n+1, k) = k*S(n, k) + S(n, k-1)`.
- Given a set of n elements, find number of ways of partitioning it. 
Examples: 
```
Input:  n = 2
Output: Number of ways = 2
Explanation: Let the set be {1, 2}
            { {1}, {2} } 
            { {1, 2} }
```
## 📈 Workflow of the script
- `bellNumber` -- This is the working function which will check and return the nth bell numbers one after another using the Dynamic Programming method.
- `main` - This is the driver program for this script.

## 📃 Explanation
When we add a (n+1)’th element to k partitions, there are two possibilities. 
1) It is added as a single element set to existing partitions, i.e, S(n, k-1) 
2) It is added to all sets of every partition, i.e., k*S(n, k)
S(n, k) is called Stirling numbers of the second kind
First few Bell numbers are 1, 1, 2, 5, 15, 52, 203, …. 
A Simple Method to compute n’th Bell Number is to one by one compute S(n, k) for k = 1 to n and return sum of all computed values. Refer this for computation of S(n, k).
A Better Method is to use Bell Triangle. Below is a sample Bell Triangle for first few Bell Numbers. 
```
1
1 2
2 3 5
5 7 10 15
15 20 27 37 52
```

## 🧮 Algorithm
The triangle is constructed using below formula. 
```
// If this is first column of current row 'i'
If j == 0
   // Then copy last entry of previous row
   // Note that i'th row has i entries
   Bell(i, j) = Bell(i-1, i-1) 

// If this is not first column of current row
Else 
   // Then this element is sum of previous element 
   // in current row and the element just above the
   // previous element
   Bell(i, j) = Bell(i-1, j-1) + Bell(i, j-1)
```

**Interpretation :**
Then Bell(n, k) counts the number of partitions of the set {1, 2, …, n + 1} in which the element k + 1 is the largest element that can be alone in its set.
For example, Bell(3, 2) is 3, it is count of number of partitions of {1, 2, 3, 4} in which 3 is the largest singleton element. There are three such partitions:
```
    {1}, {2, 4}, {3}
    {1, 4}, {2}, {3}
    {1, 2, 4}, {3}. 
```
## 💻 Input and Output 
- **Test Case 1 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Bell%20Numbers/Images/bell1.png)

- **Test Case 2 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Bell%20Numbers/Images/bell2.png)

- **Test Case 3 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Bell%20Numbers/Images/bell3.png)


## ⏰ Time and Space complexity
- **Time Complexity:** `O(n^2)`.

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2021 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
