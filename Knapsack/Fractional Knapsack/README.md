# Fractional Knapsack Problem using Brute Force Method
Language used : **Python 3**

## 🎯 Aim
The aim of this script is to find out the maximum total value in the knapsack.

## 👉 Purpose
The main purpose of this script is to show the implementation of Brute Force Method to find out the maximum total value in the knapsack.

## 📄 Description
Given weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In the 0-1 Knapsack problem, we are not allowed to break items. We either take the whole item or don’t take it. 
```
Input: 
Items as (value, weight) pairs 
arr[] = {{60, 10}, {100, 20}, {120, 30}} 
Knapsack Capacity, W = 50; 

Output: 
Maximum possible value = 240 
by taking items of weight 10 and 20 kg and 2/3 fraction 
of 30 kg. Hence total price will be 60+100+(2/3)(120) = 240
```

## 📈 Workflow of the script
- `ItemValue` - This function returns the item values of the data class.
- `FractionalKnapSack` - This function is the main architecture to solve the program.
- `__main__` - This is the driver code of the script.

## 📃 Explanation
In Fractional Knapsack, we can break items for maximizing the total value of knapsack. This problem in which we can break an item is also called the fractional knapsack problem. 
```
Input : Same as above 
Output : Maximum possible value = 240 By taking full items of 10 kg, 20 kg and 2/3rd of last item of 30 kg
```
A brute-force solution would be to try all possible subset with all different fraction but that will be too much time taking. 

## 🧮 Algorithm
- An efficient solution is to use Greedy approach. The basic idea of the greedy approach is to calculate the ratio value/weight for each item and sort the item on basis of this ratio.
- Then take the item with the highest ratio and add them until we can’t add the next item as a whole and at the end add the next item as much as we can. Which will always be the optimal solution to this problem.
- A simple code with our own comparison function can be written as follows, please see sort function more closely, the third argument to sort function is our comparison function which sorts the item according to value/weight ratio in non-decreasing order.
- After sorting we need to loop over these items and add them in our knapsack satisfying above-mentioned criteria.

## 💻 Input and Output 
```
- Fractional Knapsack Problem using Brute Force Method - 
-----------------------------------------------------

The values given : 
[60, 40, 100, 120]
-----------------------------------------------------
The corresponding weights are :
[10, 40, 20, 30]
-----------------------------------------------------
The maximum capacity can be : 
50

-----------------------------------------------------

Output : 
Maximum value in Knapsack = 240.0
```

![](https://github.com/abhisheks008/PyAlgo-Tree/blob/main/Knapsack/Fractional%20Knapsack/Images/frac1.PNG)


## ⏰ Time and Space complexity
- **Time Complexity:** `O(n log n)`.

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2021 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
