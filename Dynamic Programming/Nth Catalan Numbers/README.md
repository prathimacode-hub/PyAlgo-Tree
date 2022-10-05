# Nth Catalan Numbers using Dynamic Programming
Language used : **Python 3**

## 🎯 Aim
The aim of this script is to find out the n'th catalan numbers using Dynamic Programming.

## 👉 Purpose
The main purpose of this script is to show the implementation of Dynamic programming on finding out the n'th catalan numbers.

## 📄 Description
Catalan numbers are defined as a mathematical sequence that consists of positive integers, which can be used to find the number of possibilities of various combinations. 

**Examples:**  
```
Input  : k = 12
Output : 1 1 2 5 14 42 132 429 1430 4862 16796 58786 

Input  : k = 10
Output : 1 1 2 5 14 42 132 429 1430 4862 

Input  : k = 8
Output : 1 1 2 5 14 42 132 429 
```

## 📈 Workflow of the script
- `catalan` - The main function of the script to find out the catalan numbers using Dynamic Approach.
- `main` - This is the driver code for this code/script.
- `k` - User given integer which signifies the upper range of the Catalan series.

## 🧮 Algorithm
Let's see how it works,
- Create an array `catalan[]` for storing `ith` Catalan number.
- Initialize, `catalan[0]` and `catalan[1]` = 1
- Loop through `i = 2` to the given Catalan number `n`.
- Loop throught `j = 0` to `j < i` and Keep adding value of `catalan[j] * catalan[i – j – 1]` into `catalan[i]`.
- Finally, `return catalan[n]`.

## 💻 Input and Output 
- **Test Case 1 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Nth%20Catalan%20Numbers/Images/catalan-1.png)

- **Test Case 2 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Nth%20Catalan%20Numbers/Images/catalan-2.png)

- **Test Case 3 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Nth%20Catalan%20Numbers/Images/catalan-3.png)


## ⏰ Time and Space complexity
- **Time Complexity:** `O(n^2)`. 
- **Space Complexity:** `O(n)`.

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2022 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
