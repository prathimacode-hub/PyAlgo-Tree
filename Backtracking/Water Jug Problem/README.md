# Water Jug Problem

## Aim

The aim is to solve Water Jug Problem using BFS or DFS as per user's choice.


## Purpose

Given Problem: You are given a 'm' liter jug and a 'n' liter jug where '0<m<n'. Both the jugs are initially empty. The jugs don't have markings to allow measuring smaller quantities. You have to use the jugs to measure 'd' liters of water where 'd<n'. Determine the minimum no of operations to be performed to obtain 'd' liters of water in one of jug. The **purpose** is to come up with a solution for this problem.


## Short description of package/script

- The problem is solved by BFS/DFS as per user's choice.
- Backtracking is used for keeping track of all the visited nodes and possible solutions.
- Complete steps get printed with each and every state mentioned.


## Workflow of the Project

Description of functions used in the code and their purpose: 

get_search_type --> This method accepts an input for asking the choice for type of searching required i.e. BFS or DFS.

get_jugs --> This method accept volumes of the jugs as an input from the user.

get_goal --> This method returns the desired amount of water as goal.

is_goal --> This method checks whether the given path matches the goal node.

been_there --> This method validates whether the given node is already visited.

next_transitions --> This method returns the list of all possible transitions.

print_path --> This method prints the goal path.

search --> This method searches for a path between starting node and goal node.

After the desired values are entered by the user, the 'search' function is called to find the path/solution (if one exists).

## Compilation Steps

After the script is run, enter:
1. The volume for first jug.
2. The volume of secong jug.
3. The desired amount of water.
4. Choose the search technique.
That's it! All the steps to the goal state (if found) will be listed.


## Output

<img width = 300 height = 600 src="../Water Jug Problem/Images/ss1.png">
<img width = 300 height = 600 src="../Water Jug Problem/Images/ss2.png">
<img width = 300 height = 600 src="../Water Jug Problem/Images/ss3.png">
<img width = 300 height = 200 src="../Water Jug Problem/Images/ss4.png">

## Author

[Manasi Chhibber](https://github.com/Manasi2001)
