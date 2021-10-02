# 0/1 Knapsack
Language used : **Python3**

## 🎯 Aim
To maximize profit/value in 0/1 Knapsack Problem

## 🌟 Purpose
To show the implementation of Top Down Dynamic Programming approach to solve 0/1 Knapsack Problem.

## 📄 Description
The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, take items to include in a knapsack such that the total weight is less than or equal to a given limit and the total value is as large as possible. Print the total value.

Example:
```
Input :
val = [60, 100, 120 ]
wt = [10, 20, 30 ]
W = 50

Output :
220
```

## 🧮 Explanation
A basic brute-force solution could be to try all combinations of the given items, allowing us to choose the one with maximum profit and a weight that doesn’t exceed ‘W.’ Take the example of 3 items, as shown in the diagram below. To try all the combinations, our algorithm will look like:

<div align="center">
<img src="https://user-images.githubusercontent.com/72177954/135701909-41ccb37f-6280-4fec-b144-de4a48989b24.jpg">
</div></br>

We can optimize this algorithm further with a 2D matrix. We can overcome the problem of calculating redundant cases and thus increased complexity. We can solve this problem by simply creating a 2-D array that can store a particular state (n, w) if we get it the first time. Now if we come across the same state (n, w) again instead of calculating it in exponential complexity we can directly return its result stored in the table in constant time. This method gives an edge over the recursive approach in this aspect.

```
Let weight elements = {1, 2, 3}
Let weight values = {10, 15, 40}
Capacity=6

We intialize a 2D MATRIX called DP with 0 to 3(no of items) rows and 0 to 6(max capacities possible)
Each cell of this DP will represent max profit by selecting certain combination of items(through recursion)
which is below or equal to max capacity of it's column, We initialize all cell values as -1.

Since we know our 2d dp matrix will be as shown below irrespective of the values of weights as 
not taking any element or max capacity=0 will give max profit = 0 so 0th row and 0th column are 
0, consider -1 to be null values:
    0   1   2   3   4   5   6  (max capacities)
    -   -   -   -   -   -   -
0 | 0   0   0   0   0   0   0

1 | 0  

2 | 0  

3 | 0  
(item no.)

Filling 1st row:
For filling 'weight(i) = 1' we come across 'j = 1 to 6' in which we take maximum of :
max(0, 0 + DP[1-1][j-1]) = 25, from j = 1 to 6, where 0=DP[i-1][j] in 1 not taken.
    |        |
   '1'      '1 taken'
 not taken  

    0   1   2   3   4   5   6
    -   -   -   -   -   -   -
0 | 0   0   0   0   0   0   0

1 | 0  10  10  10  10  10  10

2 | 0  

3 | 0  
 
Filling 2nd row:
For filling 'weight(i) = 2' at 'j = 1' we take maximum of :
max(10, 15 + DP[2-1][1-2]) = 10, where 10 = DP[i-1][j] and since for "15 + DP[2-1][1-2]" we will reach max weight limit 
    |        |                   so it cannot be taken, that why DP[2-1][1-2] is undefined and also not accessed
   '2'      '2 taken'
 not taken   
 
For filling 'weight(i) = 2' at 'j = 2' we take maximum of :
max(10, 15 + DP[2-1][2-2]) = 15, where 10 = DP[i-1][j]
    |        |
   '2'      '2 taken'
 not taken  
 
For filling 'weight(i) = 2' at 'j = 3 to 6' we take maximum of :
max(10, 15 + DP[2-1][j-2]) = 25, where 10 = DP[i-1][j], and since all DP[1][1] to DP[1][6] has value 10, so 15+10=25
    |        |
   '2'      '2 taken'
 not taken  

    0   1   2   3   4   5   6
    -   -   -   -   -   -   -
0 | 0   0   0   0   0   0   0

1 | 0  10  10  10  10  10  10

2 | 0  10  15  25  25  25  25

3 | 0  
 
Filling 3rd row:
For filling 'weight(i) = 3' at 'j = 1' we take maximum of :
max(10, 40 + DP[3-1][1-3]) = 15, where 10 = DP[i-1][j], and since DP[3-1][1-3] isnt valid we take 10 as max
    |        |
   '3'      '3 taken'
 not taken  

For filling 'weight(i) = 3' at 'j = 2' we take maximum of :
max(15, 40 + DP[3-1][2-3]) = 15, where 10 = DP[i-1][j], and since DP[3-1][2-3] isnt valid we take 15 as max
    |        |
   '3'      '3 taken'
 not taken  

For filling 'weight(i) = 3' at 'j = 3' we take maximum of :
max(25, 40 + DP[3-1][3-3]) = 15, where 10 = DP[i-1][j], and since DP[3-1][3-3] is valid we take 40+0 as max
    |        |
   '3'      '3 taken'
 not taken  
 
similarly, when we reach 'weight(i) = 3' at 'j = 6' we take maximum of :
max(25, 40 + DP[3-1][3-3]) = 15, where 10 = DP[i-1][j], and since DP[6-1][6-3] is valid we take 40+25 as max
    |        |
   '3'      '3 taken'
 not taken
We have reached our solution for max profit (with max weight capacity = 6) at DP[3][6] (the last cell of our 2d matrix)

    0   1   2   3   4   5   6
    -   -   -   -   -   -   -
0 | 0   0   0   0   0   0   0

1 | 0  10  10  10  10  10  10

2 | 0  10  15  25  25  25  25

3 | 0  10  15  40  50  55  65
```
## 💻 Input and Output 
- **Test Case 1 :**

![io 1](https://user-images.githubusercontent.com/72177954/135707806-ee72b296-541a-462a-ab9f-d3e4fabc31b8.png)

- **Test Case 2 :**

![io 2](https://user-images.githubusercontent.com/72177954/135707940-3e153cc4-d1cd-4bc2-b518-f8a1bb294ed3.png)

## ⏰ Time and Space complexity
- **Time Complexity:** `O(N*W)`. 
- **Space Complexity:** `O(N*W)`.

## Author
Neeraj Pratap Hazarika [@NeerajHazarika](https://github.com/NeerajHazarika)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
