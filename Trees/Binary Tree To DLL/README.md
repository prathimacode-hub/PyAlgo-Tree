
# Binary Tree To Doubly Linked List


## Aim

The aim is to create a python code to convert a given binary tree to a doubly linked list in-place base on in-order traversal


## Purpose

The purpose is to come up with an efficient solution (if any)

## Short description of project

The project defines a binary tree, 
which then is passed to a function, where it is converted to a doubly linked list by recursive approach and returned to a new variable,
then the answer is printed.

## Workflow of the Project

Description of functions used in the code and their purpose:

Node --> Class, to define node of the binary tree and dll, has data, left, and right as attributes

binary_tree_to_dll --> Function, takes in tree root, head and tail pointer of DLL, recursively calls the subtrees converting the tree to list, returns the sum

print_list --> Function, iterates over the linked list from head passed as argument and prints the data elements

After the tree root is passed to the binary_tree_to_dll function, control is passed to that function, it uses the reccursive approach to convert the tree, 
first left subtree is converted, then pointers are manipulated to make a chain between current node and the tail of the linked list, finally converting the right subtree.
The function returns the head of the linked list, which is then used with print_list function to print.

## Required libraries

none 

## Compilation Steps
Run the script, after that :

 1. The tree is made manually here, to focus on conversion part 
 2. The program returns the equivalent doubly linked list to the driver code
 3. The program is then run to print the linked list



# Output

<img width = 800 height = 120 src="../Binary Tree To DLL/Images/binary_tree_to_dll_output1.PNG">
<img width = 800 height = 120 src="../Binary Tree To DLL/Images/binary_tree_to_dll_output2.PNG">
<img width = 800 height = 120 src="../Binary Tree To DLL/Images/binary_tree_to_dll_output3.PNG">




## Author
[Pushpit Jain](https://github.com/pushpit-J19)
