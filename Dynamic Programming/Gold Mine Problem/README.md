# Gold Mine Problem using Dynamic Programming
Language used : **Python 3**

## 🎯 Aim
The aim of this script is to find out the maximum amount of gold that can be collected from the gold mine.

## 👉 Purpose
The main purpose of this script is to show the implementation of Dynamic Programming to find out the maximum amount of gold can be collected from the gold mine.

## 📄 Description
Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. Initially the miner is at first column but can be at any row. He can move only `(right->,right up /,right down\)` that is from a given cell, the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right. Find out maximum amount of gold he can collect. 
Examples: 
 
```
Input : mat[][] = {{1, 3, 3},
                   {2, 1, 4},
                  {0, 6, 4}};
Output : 12 
{(1,0)->(2,1)->(1,2)}

Input: mat[][] = { {1, 3, 1, 5},
                   {2, 2, 4, 1},
                   {5, 0, 2, 3},
                   {0, 6, 1, 2}};
Output : 16
(2,0) -> (1,1) -> (1,2) -> (0,3) OR
(2,0) -> (3,1) -> (2,2) -> (2,3)
```
## 🧮 Algorithm
- Create a 2-D matrix `goldTable[][])` of the same as given matrix `mat[][]`. If we observe the question closely, we can notice following. 
- Amount of gold is positive, so we would like to cover maximum cells of maximum values under given constraints.
- In every move, we move one step toward right side. So we always end up in last column. If we are at the last column, then we are unable to move right
- If we are at the first row or last column, then we are unable to move right-up so just assign 0 otherwise assign the value of `goldTable[row-1][col+1]` to right_up. If we are at the last row or last column, then we are unable to move right down so just assign 0 otherwise assign the value of `goldTable[row+1][col+1]` to right up. 
- Now find the maximum of right, right_up, and right_down and then add it with that `mat[row][col]`. At last, find the maximum of all rows and first column and return it.

## 💻 Input and Output 
- **Test Case 1 :**
```
Input Given :
{ {1, 3, 1, 5},
{2, 2, 4, 1},
{5, 0, 2, 3},
{0, 6, 1, 2}};
```

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Gold%20Mine%20Problem/Images/gold1.PNG)

- **Test Case 2 :**
```
Input Given :
{{1, 3, 3},
{2, 1, 4},
{0, 6, 4}};
```
![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Gold%20Mine%20Problem/Images/gold2.PNG)

## ⏰ Time and Space complexity
- **Time Complexity :** `O(m*n)`.
- **Space Complexity :** `O(m*n)`.

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2021 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
