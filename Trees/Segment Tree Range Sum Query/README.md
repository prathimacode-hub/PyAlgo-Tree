# Segment Tree Range Sum Query


## Aim

The aim is to create a python code to do range sum query on a segment tree of a given array of numbers
## Purpose

The purpose is to come up with an efficient solution (if any)

## Short description of project

The project takes in input the array, 
and then it is converted to a segment tree and returned to a new variable,
then queries are called to do range sum over a range and the answer is then printed

## Workflow of the Project

Description of functions used in the code and their purpose:

segment_tree_creation --> Function, takes in a list, returns corresponding segment tree

segment_tree_range_sum_query --> Function, takes in tree, lower and upper index of range whose sum is to be calculated, returns the sum

After the list is passed to the segment_tree_creation function, control is passed to that function, it uses the iterative approach to generate the segment tree and returns it, 
this segment tree is passed to the segment_tree_range_sum_query function, which calculates the sum in the given range and returns it, which is then printed

## Required libraries

math library --> for ceil and log2 functions 

## Compilation Steps
Run the script, after that :

 1. The expression is made manually here, to focus on conversion part 
 2. The program tells the equivalent segment tree
 3. The program is then run to do range sum queries, and it shows the updated array and tree



# Output

<img width = 800 height = 250 src="../Segment Tree Range Sum Query/Images/range_sum_query_output1.PNG">
<img width = 800 height = 250 src="../Segment Tree Range Sum Query/Images/range_sum_query_output2.PNG">



## Author
[Pushpit Jain](https://github.com/pushpit-J19)
