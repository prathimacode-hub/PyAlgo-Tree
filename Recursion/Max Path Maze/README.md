# Max Path Maze

## Aim

Demonstrate a Recursion backtracking technique to keep a count.


## Purpose

Run through all possible paths from any given spot to the end of 
a maze (bottem left corner of a 2D array)


## Short description of package/script

The script sets up a 2D matrix acting as a maze, it then sets a counter to 0 and sets the coordinates to the first cell of the matrix
in this case (0, 0), then calls upon the recursive function with these parameters to find available paths to the end of the maze.

## Workflow of the Project

- Descriptions of functions used in the code:
valid_cell(x, y) --> check if current cell is out of bounds or if one of the coordinates is illegal (less than 0)

count_valid_paths(maze, x, y, checked, paths) --> Recursion function, for each cell it will check the cell is valid
and try to find a path to the end of the maze from it. The maze is the 2D array, x and y are the coordinates, checked is a 2D matrix to 
keep track of visited cells and paths is the counter for the number of paths


## Compilation Steps

Run the script in order to see available paths at a given maze, feel free to edit the maze
or the starting point to get diffrent results

## Output

<img width = 300 height = 100 src="../Max Path Maze/Images/terminal_output.PNG">

## Author(s)
Yarden Galon