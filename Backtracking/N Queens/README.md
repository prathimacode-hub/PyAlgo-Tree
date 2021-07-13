# N Queens

## Aim

To place N queens in a N*N Chessboard such that no two queens attack each other. A queen is said to be attacked by another queen if they share same diagonal(right/left), Row or Column.


## Purpose

The purpose is to come up with a solution for this problem (if possible) using backtracking.


## Short description of package/script

- Based on user's choice, the size of the chessboard is decided.
- Backtracking is used for keeping track of all the possible positions on the chessboard.
- If a solution is possible, it is printed out.


## Workflow of the Project

Description of functions used in the code and their purpose:

n_queens --> Method to keep track of occupied and vacant places.

place_queen --> Recursive method to find vacant spaces and place the queens.

After the desired values are entered by the user, the 'n_queen' function checks for vacant spaces and then for finding solution, the control is shifted to 'place_queen' function.


## Compilation Steps

After the script is run, enter:

1. Board size.

That's it! If the solution is possible, it will get printed.


## Output

<img src="../N Queens/Images/ss.png">


## Author

[Manasi Chhibber](https://github.com/Manasi2001)
