# Trapping Rainwater 

## Aim

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

## Purpose

The purpose is to work with arrays.


## Short description of package/script

- Traverse the array from left to right.
- For every element, traverse the array from start to that index and find the maximum height and traverse the array from the current index to end, and find the maximum   height.
-  The amount of water that will be stored in this column is minimum of both the heights – array[i], add this value to the total amount of water stored.
-  Print the total amount of water stored.


## Workflow of the Project

Description of functions used in the code and their purpose:

maxWater- Function to find maximum water stored.
The input is sent to the function which returns the result.


## Compilation Steps

After the script is run, enter:

1. Size of Array.
2. Elements of array.

The maximum water stored is printed.


## Output

![](Images/outputimg5.jpg)


## Author

[SiddhiBhanushali](https://github.com/siddhi-244)
