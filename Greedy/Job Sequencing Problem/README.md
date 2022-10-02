# Job Sequencing Problem using Greedy Approach
🔴 Language used : **Python 3**

## 🎯 Aim
The aim of this script is to find the maximum profit earned by executing the tasks within the specified deadlines.

## 👉 Purpose
The main purpose of this script is to show the implementation of Greedy Approach to find the maximum profit earned by executing the tasks within the specified deadlines.

## 📄 Description
Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. It is also given that every job takes a single unit of time, so the minimum possible deadline for any job is 1. Maximize the total profit if only one job can be scheduled at a time.

🔴 Examples: 

```
Constraints:
arr[] -> Set of datapoints including JobID, Deadline and Profit into a single array.
t -> No. of jobs to be scheduled.

Input:  
Five Jobs with following deadlines and profits

JobID   Deadline  Profit
  a        2       100
  b        1       19
  c        2       27
  d        1       25
  e        3       15

Output: 
Following is maximum profit sequence of jobs: 
c, a, e
```


## 🧮 Algorithm
Greedily choose the jobs with maximum profit first, by sorting the jobs in decreasing order of their profit. This would help to maximize the total profit as choosing the job with maximum profit for every time slot will eventually maximize the total profit.
- This problem is basically solved using the `printJobScheduling(arr, t)` funtion, which is basically the main function. `arr` signifies the job array and `t` signifies the number of jobs to be scheduled.
- Sort all jobs in decreasing order of profit. 
- Iterate on jobs in decreasing order of profit.For each job , do the following :
  - Find a time slot `i`, such that slot is empty and `i < deadline` and `i` is greatest. Put the job in this slot and mark this slot filled. 
  - If no such `i` exists, then ignore the job. 
- This whole process will be repeated until and unless the funtion got the `-1` value. Once it got the `-1` value it will stop the program and provide the output.

## 💻 Input and Output 
- **Test Case 1 :**
```
Input Given :
arr = [['a', 2, 100],
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]
```

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Greedy/Job%20Sequencing%20Problem/Images/jsp-1.png)

- **Test Case 2 :**
```
Input Given :
arr = [['a', 4, 20], 
       ['b', 1, 10],
       ['c', 1, 40],
       ['d', 1, 30]]
```
![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Greedy/Job%20Sequencing%20Problem/Images/jsp-2.png)

## ⏰ Time and Space complexity
- **Time Complexity :** `O(n^2)`.
- **Space Complexity :** `O(n)`.

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2022 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
