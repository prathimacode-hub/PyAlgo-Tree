# Activity Selection Problem using Greedy Approach
🔴 Language used : **Python 3**

## 🎯 Aim
The aim of this script is to find out the maximum number of activities to be performed by a single person in between the start and finish time given in the problem.

## 👉 Purpose
The main purpose of this script is to show the implementation of Greedy Approach to find out the maximum number of activities to be performed by a single person in between the start and finish time given in the problem.

## 📄 Description
You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. 

Suppose `S = {1, 2....n}` is the set of n proposed activities. The activities share resources which can be used by only one activity at a time, e.g., Tennis Court, Lecture Hall, etc. Each Activity `i` has start time si and a finish time `fi`, where `si ≤fi`. If selected activity `i` take place meanwhile the half-open time interval `[si,fi)`. Activities `i` and `j` are compatible if the intervals `(si, fi)` and `[si, fi)` do not overlap (i.e. `i` and `j` are compatible if `si≥fi` or `si≥fi)`. The activity-selection problem chosen the maximum-size set of mutually consistent activities.

🔴 Examples: 

```
Constraints:
start[] -> an array of start time for the activities.
finish[] -> an array of finish time for the activities.
output[] -> an array of maximum set of activities to be done by a person.

Input:
Consider the following 6 activities  sorted by finish time.

start[]  =  {1, 3, 0, 5, 8, 5};
finish[] =  {2, 4, 6, 7, 9, 9};

Output:
A person can perform at most four activities. The maximum set of activities that can be executed is {0, 1, 3, 4} 
[These are indexes in start[] and finish[]]
```

## 📊 Flowchart
```
printMaxActivities(s, f)
1. n ← length [s]
2. A ← {1}
3. j ← 1.
4. for i ← 2 to n
5. do if si ≥ fi
6. then A ← A ∪ {i}
7. j ← i
8. return A
```

## 🧮 Algorithm
- This algorithm is called Greedy-Iterative-Activity-Selector, because it is first of all a greedy algorithm, and then it is iterative. There's also a recursive version of this greedy algorithm.
- Sorts in increasing order of finish times the array of activities `A` by using the finish times stored in the array `f`. This operation can be done in `O(n log n)` time, using for example merge sort, heap sort, or quick sort algorithms.
- Creates a set `S` to store the selected activities, and initialises it with the activity that has the earliest finish time.
- Creates a variable `k` that keeps track of the index of the last selected activity.
- Starts iterating from the second element of that array `A` up to its last element.
- If the start time `s[i]` of the `ith` activity `A[i]` is greater or equal to the finish time `f[k]` of the last selected activity `A[k]`, then `A[i]` is compatible to the selected activities in the set `S`, and thus it can be added to `S`.
- The index of the last selected activity is updated to the just added activity `A[i]`.


## 💻 Input and Output 
- **Test Case 1 :**
```
Input Given :
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
```

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Greedy/Activity%20Selection%20Problem/Images/asp-1.png)

- **Test Case 2 :**
```
Input Given :
s = [1, 2, 3, 4, 7, 8, 9, 9, 11, 12]
f = [3, 5, 4, 7, 10, 9, 11, 13, 12, 14]
```
![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Greedy/Activity%20Selection%20Problem/Images/asp-2.png)

## ⏰ Time and Space complexity
- **Time Complexity :** `O(n)`.
- **Space Complexity :** `O(1)`.

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2022 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
