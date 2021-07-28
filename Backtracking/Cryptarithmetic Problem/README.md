# Cryptarithmetic Problem

## Aim

Cryptarithmetic problems are mathematical puzzles where digits are replaced by symbols. The aim is to find unique digits(0-9) that the letters should represent, such that they satisfy the given constraints.


## Purpose

The purpose is to come up with a solution for SEND MORE MONEY Cryptarithmetic problem using backtracking.


## Short description of package/script

The cryptarithmetic problem that is needed to be solved here is:
    
<img width = 150 height = 200 src = "https://www.puzzleprime.com/wp-content/uploads/2018/09/DudeneySendMoreMoney.png">

Distinct variables are: S, E, N, D, M, O, R, Y

Domain: {0,...,9}


## Workflow of the Project

Description of functions used in the code and their purpose:

add_constraint --> This method adds constraint to variables as per their domains.

consistent --> This method checks if the value assignment is consistent by checking all constraints.

backtracking_search --> This method is performing the backtracking search to find the result.

satisfied --> This method makes sure that only unique values get assigned. If there are duplicate values then it's not a solution.


## Compilation Steps

Just run the script and solution will get printed. You'll see a unique number from 0-9 associated with each unique alphabet.


## Output

<img src="../Cryptarithmetic Problem/Images/ss.png">


## Author

[Manasi Chhibber](https://github.com/Manasi2001)
