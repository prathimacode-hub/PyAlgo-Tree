
#  Solving 8-puzzle problem using A* algorithm

The 8-puzzle consists of an area divided into 3x3 (3 by 3) grid. Each grid with in the puzzle
is known as tile and each tile contains a number ranged between 1 to 8, so that they can be
uniquely identified. Tile adjacent to the empty grid can be moved to the empty space leaving
its previous position empty until reaching the goal.

# PROBLEM FORMULATION
- Goal: Goal State is initially given.
- State: Instance of Puzzle.
- Actions: Move the blank tile in left, up, down and right positions
- Performance: Number of total moves in the solution

# A* ALGORITHM

A* is an informed search algorithm used in path findings and graph traversals. It is a
combination of uniform cost search and best first search, which avoids expanding expensive
paths. A* star uses admissible heuristics which is optimal as it never over-estimates the path
to goal. The evaluation function A* star uses for calculating distance is

- f(n) = g(n) + h(n)
- g(n) = cost so far to reach n
- h(n) = estimated cost from n to goal
- f(n) = estimated total cost of path through n to goal

# Heuristic Functions
The heuristic function is a way to inform the search regarding the direction to a goal. It provides
an information to estimate which neighboring node will lead to the goal. The two heuristic
functions that we considered for solving 8-puzzle problem are
