# 8 Puzzle Problem using BFS

## Aim

An instance of the n-puzzle game consists of a board holding n^{2}-1 distinct movable tiles, plus an empty space. The tiles are numbers from the set 1,..,n^{2}-1. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it. In this assignment, the blank space is going to be represented with the number 0. Given an initial state of the board, the combinatorial search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending order 0,1,..,n^{2}-1.


## Purpose

The purpose is to solve this problem using BFS Algorithm.


## Short description of package/script

The goal state that we want to reach is:

[1, 2, 3]

[8, 0, 4]

[7, 6, 5] 

The search space is the set of all possible states reachable from the initial state. The blank space may be swapped with a component in one of the four directions {‘Up’, ‘Down’, ‘Left’, ‘Right’}, one move at a time.


## Workflow of the Project

The search begins by visiting the root node of the search tree, given by the initial state. Among other book-keeping details, three major things happen in sequence in order to visit a node:

- First, we remove a node from the frontier set.

- Second, we check the state against the goal state to determine if a solution has been found.

- Finally, if the result of the check is negative, we then expand the node. To expand a given node, we generate successor nodes adjacent to the current node, and add them to the frontier set. Note that if these successor nodes are already in the frontier, or have already been visited, then they should not be added to the frontier again.


## Compilation Steps

Once the script is run, all the states from the initial to the final are printed along with the move for each and every step.


## Output

<img src="../8 Puzzle Problem using BFS/Images/ss1.png">
<img src="../8 Puzzle Problem using BFS/Images/ss2.png">
<img src="../8 Puzzle Problem using BFS/Images/ss3.png">
<img src="../8 Puzzle Problem using BFS/Images/ss4.png">   


## Author

[Manasi Chhibber](https://github.com/Manasi2001)
