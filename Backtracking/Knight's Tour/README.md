# Knight's Tour

## Aim

To check whether it is possible for a Knight to visit each cell of the N*N chessboard without visiting any cell twice starting from (X, Y) position.


## Purpose

The purpose is to come up with a solution for this problem (if possible) using backtracking.


## Short description of package/script

- Based on user's choice, the size of the chessboard is decided.
- Backtracking is used for keeping track of all visited places on the chessboard.
- If a solution is possible, it is printed out.


## Workflow of the Project

Description of functions used in the code and their purpose:

move_Knight --> The method to position knight on various coordinates according to the 2+1/2 step move style.

Knight_Tour --> The method to allot a set of possible moves and keep track of all the visited places on the chessboard.

After the desired size of chessboard is entered by the user, 'Knight_Tour' function is called to check for the validity of moves and 'move_Knight' to place the knight on all possible coordinates.


## Compilation Steps

After the script is run, enter:

1. The desired chessboard size.

That's it! If the solution is possible, it will get printed.


## Output

<img src="../Knight's Tour/Images/ss.png">


## Author

[Manasi Chhibber](https://github.com/Manasi2001)


