Queue in Python


Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner. With a queue the least recently added item is removed first. A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.
 
  



Operations associated with queue are: 
 
* Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
* Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
* Front: Get the front item from queue – Time Complexity : O(1)
* Rear: Get the last item from queue – Time Complexity : O(1)
 






Implementation
There are various ways to implement a queue in Python. This article covers the implementation of queue using data structures and modules from Python library.
Queue in Python can be implemented by the following ways:
1.list
2.collections.deque
3.queue.Queue


Implementation using list
List is a Python’s built-in data structure that can be used as a queue. 
Instead of enqueue() and dequeue(), append() and pop() function is used. 
However, lists are quite slow for this purpose because inserting or deleting an element at the beginning requires shifting all of the other elements by one,
 requiring O(n) time.