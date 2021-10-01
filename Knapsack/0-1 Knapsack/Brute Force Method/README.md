# 0-1 Knapsack Problem using Brute Force Method
Language used : Python 3

## 📃 Approach 
A simple solution is to consider all subsets of items and calculate the total weight and value of all subsets. Consider the only subsets whose total weight is smaller than W. From all such subsets, pick the maximum value subset.
Optimal Sub-structure: To consider all subsets of items, there can be two cases for every item. 

- **Case 1:** The item is included in the optimal subset.
- **Case 2:** The item is not included in the optimal set.

Therefore, the maximum value that can be obtained from ‘n’ items is the max of the following two values. 
- Maximum value obtained by n-1 items and W weight (excluding nth item).
- Value of nth item plus maximum value obtained by n-1 items and W minus the weight of the nth item (including nth item).

If the weight of ‘nth’ item is greater than ‘W’, then the nth item cannot be included and Case 1 is the only possibility.

## 🧮 Algorithm
It should be noted that the above function computes the same sub-problems again and again. See the following recursion tree, K(1, 1) is being evaluated twice. The time complexity of this naive recursive solution is exponential (2^n).  

```
In the following recursion tree, K() refers 
to knapSack(). The two parameters indicated in the
following recursion tree are n and W.
The recursion tree is for following sample inputs.
wt[] = {1, 1, 1}, W = 2, val[] = {10, 20, 30}
                       K(n, W)
                       K(3, 2)  
                   /            \ 
                 /                \               
            K(2, 2)                  K(2, 1)
          /       \                  /    \ 
        /           \              /        \
       K(1, 2)      K(1, 1)        K(1, 1)     K(1, 0)
       /  \         /   \              /        \
     /      \     /       \          /            \
K(0, 2)  K(0, 1)  K(0, 1)  K(0, 0)  K(0, 1)   K(0, 0)
Recursion tree for Knapsack capacity 2 
units and 3 items of 1 unit weight.
```

## ⏰ Complexity Analysis: 
- **Time Complexity:** `O(2^n)`. [As there are redundant subproblems.]
- **Auxiliary Space :** `O(1)`. [As no extra data structure has been used for storing values.]

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2021 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
