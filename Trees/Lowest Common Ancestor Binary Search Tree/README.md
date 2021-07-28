
# Lowest Common Ancestor Binary Search Tree


## Aim

The aim is to create a python code to find the Lowest Common Ancestor (LCA) of two nodes in a binary search tree, if it exists


## Purpose

The purpose is to come up with an efficient solution (if any)

## Short description of project

The project defines a binary search tree, 
which is then passed to a function with 2 nodes, which first checks if both the elements exist in the tree or not,
based on that LCA is calculated and returned in another function by recursively traversing the tree
which is then printed with a proper output.

## Workflow of the Project

Description of functions used in the code and their purpose:

Node --> Class, to define node of the binary tree, has data, left, and right as attributes

lowest_common_ancestor_binary_search_tree --> Function, takes in tree root, and both the numbers whose LCA is to be found, checks if both the elements exist in the tree or not, returns LCA or None based on existence

exists_in_tree --> Function, recursively traverses the tree, to find element, takes root and element as argument, returns True or False for existing node and non existing node respectively

find_lca --> Function, recursively finds and returns the LCA of the two numbers passed, based on the current root passed as argument 

print_output --> Function, prints the LCA value passed based on the value, with a proper message

After the tree root is passed to the lowest_common_ancestor_binary_search_tree function, control is passed to that function, it checks existence of elements by calling exists_in_tree function on both the elements which recursively traverses the tree and returns True or False based on ans , 
if they dont exist lowest_common_ancestor_binary_search_tree returns None, if they exist lowest_common_ancestor_binary_search_tree calls find_lca function,
in find_lca function, LCA of both the numbers is calculated and returned to lowest_common_ancestor_binary_search_tree, which returns the LCA to Driver code,
where it is saved in a variable, and passed to print_output function, which prints it with a proper message.

## Required libraries

none 

## Compilation Steps
Run the script, after that :

 1. The BST is made manually here, to focus on finding part 
 2. The program returns the LCA calculated of the two numbers to the driver code
 3. The program then calls a function to print the output



# Output

<img width = 350 height = 120 src="../Lowest Common Ancestor Binary Search Tree/Images/lowest_common_ancestor_binary_search_tree_output1.PNG">
<img width = 300 height = 120 src="../Lowest Common Ancestor Binary Search Tree/Images/lowest_common_ancestor_binary_search_tree_output2.PNG">
<img width = 350 height = 120 src="../Lowest Common Ancestor Binary Search Tree/Images/lowest_common_ancestor_binary_search_tree_output3.PNG">




## Author
[Pushpit Jain](https://github.com/pushpit-J19)
