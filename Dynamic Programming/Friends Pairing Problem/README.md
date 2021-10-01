# Friends Pairing Problem using Dynamic Programming
Language used : **Python 3**

## 🎯 Aim
The aim of this script is to find out the the total number of ways in which friends can remain single or can be paired up..

## 👉 Purpose
The main purpose of this script is to show the implementation of Dynamic Programming to find the total number of ways in which friends can remain single or can be paired up.

## 📄 Description
Given n friends, each one can remain single or can be paired up with some other friend. Each friend can be paired only once. **Find out the total number of ways in which friends can remain single or can be paired up.** 

Examples: 
```
Input  : n = 3
Output : 4

Input : n = 4
Output : 10

Input : n = 6
Output : 76
```

## 📈 Workflow of the script
- `countFriendsPairing` - This is the main function which provides the number of ways friends can e single.
- `main` - This is the driver code for this code/script.

## 📃 Explanation
```
{1}, {2}, {3} : all single
{1}, {2, 3} : 2 and 3 paired but 1 is single.
{1, 2}, {3} : 1 and 2 are paired but 3 is single.
{1, 3}, {2} : 1 and 3 are paired but 2 is single.
Note that {1, 2} and {2, 1} are considered same.
```
- **Mathematical Explanation**
```
The problem is simplified version of how many ways we can divide n elements into multiple groups.
(here group size will be max of 2 elements).
In case of n = 3, we have only 2 ways to make a group: 
    1) all elements are individual(1,1,1)
    2) a pair and individual (2,1)
In case of n = 4, we have 3 ways to form a group:
    1) all elements are individual (1,1,1,1)
    2) 2 individuals and one pair (2,1,1)
    3) 2 separate pairs (2,2)
```

## 🧮 Algorithm
```
f(n) = ways n people can remain single 
       or pair up.

For n-th person there are two choices:
1) n-th person remains single, we recur 
   for f(n - 1)
2) n-th person pairs up with any of the 
   remaining n - 1 persons. We get (n - 1) * f(n - 2)

Therefore we can recursively write f(n) as:
f(n) = f(n - 1) + (n - 1) * f(n - 2)
```

## 💻 Input and Output 
- **Test Case 1 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Friends%20Pairing%20Problem/Images/friend2.PNG)

- **Test Case 2 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Friends%20Pairing%20Problem/Images/friend1.PNG)

- **Test Case 3 :**

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Dynamic%20Programming/Friends%20Pairing%20Problem/Images/friend3.PNG)

## ⏰ Time and Space complexity
- **Time Complexity:** `O(n)`. 
- **Space Complexity:** `O(n)`. 

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2021 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
