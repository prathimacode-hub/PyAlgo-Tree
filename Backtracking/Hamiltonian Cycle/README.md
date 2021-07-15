# Hamiltonian Cycle

## Aim

A Hamiltonian path (or traceable path) is a path in an undirected or directed graph that visits each vertex exactly once. A Hamiltonian cycle (or Hamiltonian circuit) is a Hamiltonian path that is a cycle. The aim is to determine the existance of a Hamiltonian Cycle in the provided undirected graph and return the path if such path exist. The nodes are numbered from 1 to N.


## Purpose

The purpose is to come up with a solution for this problem (if possible) using backtracking.


## Short description of package/script

- Based on user's choice, the graph is initialized.
- Backtracking is used for keeping track of all the nodes visited already.
- If a solution is possible, it is printed out.


## Workflow of the Project

Description of functions used in the code and their purpose:

Move_next_node --> Method to visit the next node in the cycle.

Hamiltonial_Cycle --> Method to keep a track of already visited node and the answer.

After the desired values are entered by the user, the control is given to 'Hamiltonial_Cycle' function which calls 'Move_next_node' function to recursively look for a solution.


## Compilation Steps

After the script is run, enter:

1. The number of vertex and edges.
2. The edges.

That's it! If hamiltonian cycle exists, the result will get printed.


## Output

<img src="../Hamiltonian Cycle/Images/ss.png">


## Author

[Manasi Chhibber](https://github.com/Manasi2001)
