# Subset Sum Problem using Dynamic Programming
Language used : **Python 3**

## 🎯 Aim
The aim of this script is to find out if there is a subset of the given set with sum equal to given sum.

## 👉 Purpose
The main purpose of this script is to show the implementation of Dynamic Programming to find out if there is a subset of the given set with sum equal to given sum.

## 📄 Description
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 
```
Example: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
```

## 📈 Workflow of the script
- `isSubsetSum` - Returns true if there is a subset of set[] with sum equal to given sum.
- `main` - This is the driver code for this python script.

## 📃 Explanation
We will create a 2D array of `size (arr.size() + 1) * (target + 1)` of type boolean. The state `DP[i][j]` will be true if there exists a subset of elements from `A[0….i]` with sum value = `‘j’`. The approach for the problem is: 
```
if (A[i-1] > j)
DP[i][j] = DP[i-1][j]
else 
DP[i][j] = DP[i-1][j] OR DP[i-1][j-A[i-1]]
```
1. This means that if current element has value greater than ‘current sum value’ we will copy the answer for previous cases
2. And if the current sum value is greater than the `‘ith’` element we will see if any of previous states have already experienced the `sum=’j’` OR any previous states experienced a value `‘j – A[i]’` which will solve our purpose.

## 🧮 Algorithm
The below simulation will clarify the above approach: 
```
set[]={3, 4, 5, 2}
target=6
 
    0    1    2    3    4    5    6

0   T    F    F    F    F    F    F

3   T    F    F    T    F    F    F
     
4   T    F    F    T    T    F    F   
      
5   T    F    F    T    T    T    F

2   T    F    T    T    T    T    T
```

## 💻 Input and Output 
- **Test Case 1 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Subset%20Sum%20Problem/Images/subset1.png)

- **Test Case 2 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Subset%20Sum%20Problem/Images/subset2.png)

- **Test Case 3 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Subset%20Sum%20Problem/Images/subset3.png)

- **Test Case 3 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Subset%20Sum%20Problem/Images/subset4.png)


## ⏰ Time and Space complexity
- **Time Complexity:** `O(sum*n)`, where sum is the ‘target sum’ and ‘n’ is the size of array. 
- **Space Complexity:** `O(sum*n)`, as the size of 2-D array is `sum*n`.

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2021 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
