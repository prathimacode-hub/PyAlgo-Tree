<img src="../Priority Queue/Images/priority.jpg">

## Overview:
A unique kind of queue called a priority queue has elements that are each assigned a priority value. Additionally, components are treated according to their importance. In other words, more important factors come first.

## What is Priority Queue?
There must be a priority assigned to each item in the queue.
Depending on the priority order chosen by the user—that is, whether the user considers a lower number to be higher priority or a higher number to be greater priority—higher or lower priority items must be dequeued before lower or higher priority elements, respectively.
The first element that entered the priority queue first will be the first to be deleted if two items in the queue have the same priority value. This is known as the first in, first out, rule.

## Types of Priority Queue
#### Ascending Order Priority Queue:
The items in the priority queue must be similar, which means they must be either less than, equal to, or higher than one another, as was previously stated. All the components are compared to one another in an ascending order priority queue according to the following rule. The priority is applied with a higher priority to smaller elements (or numbers).

#### Descending Order Priority Queue:
All the components are compared to one another in descending order priority queue according to the following rule. The priority increases with the size of the element (or number). Eaual to one another or larger than it. All the components are compared to one another in an ascending order priority queue according to the following rule. The priority is applied with a higher priority to smaller elements (or numbers).

## Why are Heaps preferred over Binary Search Trees?
While the Self Balancing BST requires O(nLogn) time, heap construction may be completed in O(N) time. Pointers are not used anymore since heaps are built via arrays.

## Application of Priority Queue
* Djikstra's Algorithm uses t to determine the shortest route between graph nodes.
* In order to determine the Minimum Spanning Tree in a weighted undirected graph, it is employed in Prim's Algorithm.
* Heap Sort uses it to order the heap data structure.
* It is employed in the data compression algorithm Huffman Coding.

## Complexity of Priority queue
#### Time complexity:
* Insertion : O(log n)O(logn)
* Peek : O(1)O(1)
* Deletion : O(log n)O(logn)

## Read More
To read more: [Click here](https://www.scaler.com/topics/data-structures/priority-queue-in-data-structure/)
