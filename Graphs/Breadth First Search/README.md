## Overview:
Two techniques are frequently used for graph traversal: These techniques are called depth-first search (DFS) and breadth-first search (BFS), although we will just talk about BFS. Breadth-first search (BFS) is used to solve many problems, including finding the shortest path in a graph or solving puzzle games such as Rubik’s Cubes.

## What is Breadth First Search in Python?
Breadth-first search (BFS) is an algorithm for traversing graphs or trees. Breath-first search for trees and graphs are almost the same. BFS uses a queue data structure for finding the shortest path in a graph.

## Algorithm of DFS in Python
The algorithm works as follows:

* Create a queue and insert any one vertex of the graph at the back of the queue.
* Initialize a visited array and mark that vertex as visited.
* Follow the below process till the queue becomes empty:
  * Remove a front vertex from the queue.
  * Get all the adjacent vertices of the removed vertex.
  * If the adjacent vertex has not been visited, mark it as visited and insert it at the back of the queue.

## Time & Space Complexity
* Time complexity is `O(V+E)`, where V denotes the number of vertices and E denotes the number of edges. 
* Space complexity is `O(V)`.

## Input & Output
### Input:

 <img width=50% src="../Breadth First Search/Images/input.jpg"> 

```python
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D']
}
```
### Output:
 <img width=50% src="../Breadth First Search/Images/output.jpg"> 
 
```python
Breadth-first Search: A B C D E
```
