# Package/Script Name

## Aim

The main aim of the script is to sort numbers in list using shell sort.


## Purpose
The main purpose is to sort list of any numbers in O(n^2) time complexity.


## Short description of package/script

In shellSort, we make the array h-sorted for a large value of h. We keep reducing the value of h until it becomes 1. An array is said to be h-sorted if all sublists of every h’th element is sorted.


## Workflow of the Project

Gap is reduce by half in every iteration. 
In this case, we begin with n2n2 sublists. On the next pass, n4n4 sublists are sorted. Eventually, a single list is sorted with the basic insertion sort.

## Setup instructions

Install latest version of python from [python](https://www.python.org/downloads/)


## Compilation Steps

Open editor and open the file and compile the program and give input and get the desired output.


## Sample Test Cases
<h3>TEST CASE-1</h3>
<h4>Input:</h4>
1 98 3 16 3
<h5>Output:</h5>
1 3 3 16 98

<h3>TEST CASE-2</h3>
<h4>Input:</h4>
5 4 3 2 1
<h5>Output:</h5>
1 2 3 4 5

<h3>TEST CASE-3</h3>
<h4>Input:</h4>
1 1 1 0 0
<h5>Output:</h5>
0 0 1 1 1

## Output

![](https://github.com/thejaswin123/PyAlgo-Tree/blob/main/Sorting/Shell%20Sort/Images/shell_sort.png)

## Author(s)

[Thejaswin S](https://www.github.com/thejaswin123)

