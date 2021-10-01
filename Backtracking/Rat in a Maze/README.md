# Rat in a Maze Problem using Backtracking 
Language used : **Python 3**

## 🎯 Aim
The aim of this script is to find out the shortest path for the rat to reach the destination through the maze.

## 👉 Purpose
The main purpose of this script is to show the implementation of Backtracking algorithm on finding the shortest path to the destination.

## 📄 Description
- Form a recursive function, which will follow a path and check if the path reaches the destination or not. If the path does not reach the destination then backtrack and try other paths.
- Implementation of Backtracking Algorithms.

## 📈 Workflow of the script
- `printSolution` - A utility function to print solution matrix solution.
- `isSafe` - A utility function to check if x, y is valid index for N * N Maze.
- `solveMaze` - To check whether there is proper solution or not.
- `solveMazeUtil` - A recursive utility function to solve Maze problem. This is the main function of this codebase. This function solves the Maze problem using Backtracking. It mainly uses solveMazeUtil() to solve the problem. It returns false if no path is possible, otherwise return true and prints the path in the form of 1s. Please note that there may be more than one solutions, this function prints one of the feasable solutions.
- `main` - This is the driver code for this code/script.

## 📃 Explanation
A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1]. A rat starts from source and has to reach the destination. The rat can move only in two directions: forward and down. 

In the maze matrix, 0 means the block is a dead end and 1 means the block can be used in the path from source to destination. Note that this is a simple version of the typical Maze problem. For example, a more complex version can be that the rat can move in 4 directions and a more complex version can be with a limited number of moves.

For example let us take a maze and then implement the maze in the 1 and 0 manner.

![Input Image](https://github.com/prathimacode-hub/PyAlgo-Tree/blob/main/Backtracking/Rat%20in%20a%20Maze/Images/rat2.PNG)

If we convert this maze into the 1 and 0 manner then it'll be looked like this (where the 1 means open path and 0 means blocked path),
```
{1, 0, 0, 0}
{1, 1, 0, 1}
{0, 1, 0, 0}
{1, 1, 1, 1}
```
And the solution path to the destination will be like this,

![Input Image](https://github.com/prathimacode-hub/PyAlgo-Tree/blob/main/Backtracking/Rat%20in%20a%20Maze/Images/rat3.PNG)

And again if we convert the maze into the matrix format it'll be looked like this,
```
{1, 0, 0, 0}
{1, 1, 0, 0}
{0, 1, 0, 0}
{0, 1, 1, 1}

Here all the 1's are denoting the path to reach the destination!
```

## 🧮 Algorithm
1. Create a solution matrix, initially filled with 0’s.
2. Create a recursive function, which takes initial matrix, output matrix and position of `rat (i, j)`.
3. If the position is out of the matrix or the position is not valid then return.
4. Mark the position output `[i][j]` as 1 and check if the current position is destination or not. If destination is reached print the output matrix and return.
5. Recursively call for position `(i+1, j)` and `(i, j+1)`.
6. Unmark position `(i, j)`, i.e output `[i][j] = 0`.

## 💻 Input and Output 
- The input is given as,
```
The path or maze given to the rat :
1 0 0 0 
1 1 0 1 
0 1 0 0 
1 1 1 1
```

- The Output comes out as,
```
The path recognised by the algorithm :
1 0 0 0 
1 1 0 0 
0 1 0 0 
0 1 1 1
```

![](https://github.com/prathimacode-hub/PyAlgo-Tree/blob/main/Backtracking/Rat%20in%20a%20Maze/Images/rat1.PNG)

## ⏰ Time and Space complexity
- **Time Complexity:** `O(2^(n^2))`. [The recursion can run upper-bound `2^(n^2)` times.]
- **Space Complexity:** `O(n^2)`. [Output matrix is required so an extra space of size `n*n` is needed.]

---------------------------------------------------------------
## 🖋️ Author
**Code contributed by, _Abhishek Sharma_, 2021 [@abhisheks008](github.com/abhisheks008)**

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
