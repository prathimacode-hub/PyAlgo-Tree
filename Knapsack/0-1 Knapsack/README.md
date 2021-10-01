# 0-1 Knapsack Problem
Language used : **Python 3**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Knapsack/0-1%20Knapsack/Images/knapsack3.jpg)

## 🎯 Aim
The aim of this script is to find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.

## 👉 Purpose
The main purpose of this script is to show the implementation of Brute Force method and Dynamic Programming method to solve the 0-1 Knapsack problem.

## 📄 Description
Given weights and values of `n` items, put these items in a knapsack of capacity `W` to get the maximum total value in the knapsack. In other words, given two integer arrays `val[0..n-1]` and `wt[0..n-1]` which represent values and weights associated with `n` items respectively. Also given an integer `W` which represents knapsack capacity, find out the maximum value subset of `val[]` such that sum of the weights of this subset is smaller than or equal to `W`. You cannot break an item, either pick the complete item or don’t pick it `(0-1 property)`.

## 📈 Workflow of the script
- `knapsack` - This is the main function which will provide us maximum value that can be put in the capacity of W.
- `main` - This is the driver code for this code/script.

## 🧮 Algorithms and Explanation
Here to solve the 0-1 Knapsack problem, I have used two different types of methods,
- **Brute Force Method** - The brute force approach is a guaranteed way to find the correct solution by listing all the possible candidate solutions for the problem. It is a generic method and not limited to any specific domain of problems. The brute force method is ideal for solving small and simpler problems.

🔴 **You can find out the approach of Brute Force Method to solve the 0-1 Knapsack problem, [here ✔️](https://github.com/abhisheks008/PyAlgo-Tree/tree/main/Knapsack/0-1%20Knapsack/Brute%20Force%20Method)**


- **Dynamic Method** - Dynamic programming is a technique that breaks the problems into sub-problems, and saves the result for future purposes so that we do not need to compute the result again. The subproblems are optimized to optimize the overall solution is known as optimal substructure property. The main use of dynamic programming is to solve optimization problems. Here, optimization problems mean that when we are trying to find out the minimum or the maximum solution of a problem. The dynamic programming guarantees to find the optimal solution of a problem if the solution exists. The definition of dynamic programming says that it is a technique for solving a complex problem by first breaking into a collection of simpler subproblems, solving each subproblem just once, and then storing their solutions to avoid repetitive computations.

🔴 **You can find out the approach of Dynamic Method to solve the 0-1 Knapsack problem, [here ✔️](https://github.com/abhisheks008/PyAlgo-Tree/tree/main/Knapsack/0-1%20Knapsack/Dynamic%20Method)**

## 💻 Input and Output
```
The values given : 
[60, 100, 120]
-----------------------------------------------------
The corresponding weights are :
[10, 20, 30]
-----------------------------------------------------
The maximum capacity can be : 
50

-----------------------------------------------------
Output :
Maximum total value of the Knapsack : 
220
```

## 📊 Comparison of two different methods
We have implemented both the algorithms and methods and also have checked the time and  space complexities of them. The **Brute force method** is having the time complexity of `O(2^n)` and the **Dynamic Method** is having the time complexity of `O(N*W)`. From this, it is clearly visible that using **Dynamic Method** provides less time complexity which means that the program can be run smoothly with less time spent.

Hence, **Dynamic Method ✔️** is having the upper hand in between these two types of methods of solving!

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2021 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

