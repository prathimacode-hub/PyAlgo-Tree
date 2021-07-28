# Graph Coloring Problem

## Aim

Given an undirected graph and an integer M. The task is to determine if the graph can be colored with at most M colors such that no two adjacent vertices of the graph are colored with the same color.


## Purpose

The purpose is to come up with a solution for this problem (if possible) using backtracking.


## Short description of package/script

- The user enters the number of vertices, number of unique colours and the edges for the graph.
- Backtracking is used for check that all the places are filled with diferent colours according to the rule.
- If a solution is possible, 1 is printed out, else 0.


## Workflow of the Project

Description of functions used in the code and their purpose:

isSafe --> This checks whether if it safe to color the given node with a particular color i.e checking if the adjacent nodes are different from each other.

check --> This function iteratively checks different combinations.

graphcoloring --> This method assigns colors to different nodes. 

After the desired values are entered by the user, the 'graphcoloring' method is called, which sends the control to 'check' function after initializing nodes with different colours. 'isSafe' method is then called to verify that the rules are being followed.


## Compilation Steps

After the script is run, enter:

1. No. of test cases.
2. Number of vertices.
3. Total number of unu=ique colours, M.
4. All edges.

That's it! If the solution is possible, 1 will get printed, else 0 will get printed.


## Output

<img src="../Graph Coloring Problem/Images/ss.png">


## Author

[Manasi Chhibber](https://github.com/Manasi2001)
