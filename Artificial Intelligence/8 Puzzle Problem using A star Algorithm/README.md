# 8 Puzzle Problem using A star Algorithm

## Aim

An instance of the n-puzzle game consists of a board holding n^{2}-1 distinct movable tiles, plus an empty space. The tiles are numbers from the set 1,..,n^{2}-1. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it. In this assignment, the blank space is going to be represented with the number 0. Given an initial state of the board, the combinatorial search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending order 0,1,..,n^{2}-1.


## Purpose

The purpose is to solve this problem using A* Algorithm.


## Short description of package/script

The goal state that we want to reach is:

[1, 2, 3]

[8, 0, 4]

[7, 6, 5] 

The search space is the set of all possible states reachable from the initial state. The blank space may be swapped with a component in one of the four directions {‘Up’, ‘Down’, ‘Left’, ‘Right’}, one move at a time.


## Workflow of the Project

A* algorithm has 3 parameters:

g: the cost of moving from the initial cell to the current cell.

h: also known as the heuristic value, it is the estimated cost of moving from the current cell to the final cell. The actual 
   cost cannot be calculated until the final cell is reached. Hence, h is the estimated cost. We must make sure that there is 
   never an over estimation of the cost.
   
f: it is the sum of g and h. So, f = g + h

We always go to the state that has minimum 'f' value.


## Compilation Steps

Once the script is run, all the states from the initial to the final are printed along with the move for each and every step.


## Output

<img src="../8 Puzzle Problem using A star Algorithm/Images/ss.png">


## Author

[Manasi Chhibber](https://github.com/Manasi2001)
