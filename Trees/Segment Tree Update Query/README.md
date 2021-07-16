# Segment tree Update Query


## Aim

The aim is to create a python code to do update query on a segment tree of a given array of numbers to store the sums

## Purpose

The purpose is to come up with an efficient solution (if any)

## Short description of project

The project takes in input the array, 
and then it is converted to a segment tree and returned to a new variable,
then queries are called to update, which start from leaf node updating the array element,
moving up to the root node, updating the nodes.

## Workflow of the Project

Description of functions used in the code and their purpose:

segment_tree_creation --> Function, takes in a list, returns corresponding segment tree

segment_tree_update_query --> Function, takes in array, tree, index and new value to be updated, returns the updated array and tree

After the list is passed to the segment_tree_creation function, control is passed to that function, it uses the iterative approach to generate the segment tree and returns it, 
this segment tree is passed to the segment_tree_update_query function, which updates all the nodes from that array element (leaf) to the root.

## Required libraries

math library --> for ceil and log2 functions 

## Compilation Steps
Run the script, after that :

 1. The expression is made manually here, to focus on conversion part 
 2. The program tells the equivalent segment tree
 3. The program is then run to update queries, and it shows the updated array and tree



# Output

<img width = 800 height = 350 src="../Segment Tree Update Query/Images/update_query_output1.PNG">
<img width = 800 height = 350 src="../Segment Tree Update Query/Images/update_query_output2.PNG">


## Author
[Pushpit Jain](https://github.com/pushpit-J19)
