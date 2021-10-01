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

## Explanation
A basic brute-force solution could be to try all combinations of the given items (as we did above), allowing us to choose the one with maximum profit and a weight that doesn’t exceed ‘W.’ Take the example of 3 items (A, B, C, and D), as shown in the diagram below. To try all the combinations, our algorithm will look like:
```
In the following recursion tree, K() refers to knapSack(). 
The two parameters indicated in the following recursion tree are n and W. 
The recursion tree is for following sample inputs.

wt[] = {10, 20, 30}, W = 50, val[] = {10, 20, 30}

                       K(n, W)
                       K(3, 50)  
                   /            \ 
                 /                \               
            K(2, 40)                  K(2, 50)
          /       \                  /    \ 
        /           \              /        \
       K(1, 20)      K(1, 40)        K(1, 1)     K(1, 0)
       /  \         /   \              /        \
     /      \     /       \          /            \
K(0, -10)  K(0, 1)  K(0, 1)  K(0, 0)  K(0, 1)   K(0, 0)

Recursion tree for Knapsack capacity 2 units and 3 items of 1 unit weight.
```

## Author
Neeraj Pratap Hazarika [@NeerajHazarika](https://github.com/NeerajHazarika)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
