Circular Linked List
Aim
To implement Circular Linked List data structure in Python.

Purpose
The purpose is to create an alternative data structure to array.

Short description of script
A circular linked list is a sequence of individual data elements called Nodes, which are connected via links. Each data element contains a connection to another data element in the form of a pointer
A circular linked lists differs from a singly linked list because instead of the last node pointing to a null value, it instead points back to the head node.

Data Structure	        Average Insert	Average Delete	Average Search	Worst Insert	Worst Delete	Worst Search
Circular Linked List	    O(1)	        O(1)	        O(n)	        O(1)	        O(1)	        O(n)


Workflow of the Project
This script contains a class named Circular linked list. 
The Circular Linked List class contains,
Class,
_Node: Used to store data.
Methods,
traverse(),
insert_end(),
insert_beg(),
insert_mid(),
delete_beg(),
delete_end(),
delete_mid(),
list_size(),
get_prev_node(),
reverse(),
split_list(),
split_list_2().

Setup instructions
Import the script by,

from circular_linked_list import *
OR

import circular_linked_list
After import create an instance of Circular Linked List.

var = CircularLinkedList()
OR

var = circular_linked_list.CircularLinkedList()


Sample Output
After Insertion
--------------------
100
90
50
60
70
After Mid Insertion
--------------------
100
90
50
60
70
20
Before Reversal, and after deletion
--------------------
90
50
60
70
After Reversal
--------------------
70
60
50
90
After Mid Deletion
--------------------
70
60
90
List One
--------------------
70
List Two
--------------------
90
60


Author
Vishva Rana