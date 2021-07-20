"""
Linked List:
    - Linked List is a collection of node that connected through their
      references.
    - It is a linear data structure.
    - It provides faster insertion and deletion over array.

Doubly Linked List:
    Doubly Linked List is type of linked list in which every node bi-directionally
    connected with each other.

    In our implementation we use 'HEAD' and 'END' dummy nodes known as sentinels,
    for avoiding special cases in methods. By doing this we ensure every
    insertion and deletion happens in between 'HEAD' and 'END'. And we're declaring the
    Node class as protected inside main class.

:URL: https://github.com/prathimacode-hub/PyAlgo-Tree/tree/main/Lists/Doubly%20Linked%20List/doubly_linked_list.py
:Author: NanthaKumar <nknanthakumar13@gmail.com>
:Contact: https://github.com/nknantha
:Date: 2021-07-15
"""


class DoublyLinkedList:
    """
    Doubly Linked List class.

    Class:
        _Node    Protected class for node.
    Attributes:
        _head   Points the head.
        _trail  Points the end.
        _size   Stores the size.
    """

    # ------------------------------------NODE-CLASS------------------------------------- #
    class _Node:
        """
        Non-Public class for storing node.

        Attributes:
            _data  Stores node's data.
            _next  Points the next node.
            _prev  Points the previous node.
        """

        # Slots for node class.
        __slots__ = 'data', 'next', 'prev'

        def __init__(self, data=None, prev=None, next=None):
            """
            Creates node instance.

            Args:
                data: takes an object.
                prev: takes an node.
                next: takes an node.
            """
            # Initializing node attributes.
            self.data = data
            self.prev = prev
            self.next = next

        def __str__(self):
            """
            String representation of node.

            Returns: string representation of node.
            """
            return str(self.data)
    # -----------------------------------END-NODE-CLASS---------------------------------- #

    # Slots for Doubly Linked List.
    __slots__ = '_head', '_trail', '_size'

    def __init__(self, iterable=()):
        """
        Creates a Doubly Linked List instance.

        Args:
            iterable: takes an iterable object.
        """
        # Initializing node attributes.
        self._head = self._Node('HEAD')
        self._trail = self._Node('END')

        # Connecting header and trail nodes.
        self._head.next = self._trail
        self._trail.prev = self._head

        self._size = 0

        # Adding elements of iterable.
        self.extend(iterable)

    def __getitem__(self, index):
        """
        Returns the object stored in the given index.

        Args:
            index: takes an integer as index.

        Returns: the object stored in the given index.
        """
        # Raising error for slicing.
        if isinstance(index, slice):
            raise NotImplementedError('Slicing not implemented yet.')

        # Validating index.
        self._validate_index(index)

        # Walking through list and finds the index.
        node = self._head.next
        count = 0
        while node != self._trail and count < index:
            node = node.next
            count += 1

        return node.data

    def __iter__(self):
        """
        Yields elements in the Doubly Linked List.

        Yields: elements in the Doubly Linked List.
        """
        cursor = self._head.next
        while cursor != self._trail:
            yield cursor.data
            cursor = cursor.next

    def __len__(self):
        """
        Returns the size of the Doubly Linked List.

        Returns: the size of the Doubly Linked List.
        """
        return self._size

    def __repr__(self):
        """
        Returns the representation of Doubly Linked List.

        Returns: the representation of Doubly Linked List.
        """
        return f"DoublyLinkedList([{', '.join(repr(el) for el in self)}])"

    def __setitem__(self, key, value):
        """
        Store the given value at given index in Doubly Linked List.

        Args:
            key: takes an integer as index.
            value: takes an object.
        """
        # Validating index.
        self._validate_index(key)

        # Walking through list and finds the index.
        node = self._head.next
        count = 0
        while node != self._trail and count < key:
            node = node.next
            count += 1

        # Storing given value.
        node.data = value

    def __str__(self):
        """
        Returns the string representation of Doubly Linked List.

        Returns: the string representation of Doubly Linked List.
        """
        # Determining suffix part.
        suffix = ' <=> ' * bool(self._size) + 'END'
        return f"DoublyLinkedList: HEAD <=> {' <=> '.join(repr(el) for el in self)}{suffix}"

    def _delete_node(self, node):
        """
        Protected method for deleting a node in Doubly Linked List.
        And returns the data stored in that node.

        Args:
            node: takes a node in the list.

        Returns: data stored in that node.
        """
        # Marking given nodes previous and next nodes.
        previous_node = node.prev
        next_node = node.next

        # Making connections between previous and next nodes.
        previous_node.next = next_node
        next_node.prev = previous_node

        # Deprecating node and decreasing size.
        node.prev = node.next = None
        self._size -= 1

        return node.data

    def _insert_between(self, element, predecessor, successor):
        """
        A Protected method for insertion between predecessor and successor node.

        Args:
            element: takes an object.
            predecessor: takes a predecessor node.
            successor: takes a successor node.
        """
        # Creating node with predecessor and successor.
        new_node = self._Node(element, predecessor, successor)

        # Connecting the new_node between predecessor and successor.
        predecessor.next = new_node
        successor.prev = new_node

        self._size += 1

    def _validate_index(self, index):
        """
        Validates the given index and raises appropriate Errors.

        Args:
            index: takes an integer as index.
        """
        # Filtering out negative index.
        if index < 0:
            raise NotImplementedError('Negative indexing not implemented yet')

        # Handling upper boundary.
        if index >= self._size:
            raise IndexError('list index out of range')

    def append(self, element):
        """
        Appends given element in Doubly Linked List.

        Args:
            element: takes an object.
        """
        predecessor_node = self._trail.prev
        successor_node = self._trail
        self._insert_between(element, predecessor_node, successor_node)

    def clear(self):
        """
        Clears the Doubly Linked List.
        """
        if not self.is_empty():
            # Marking previous and next node.
            next_node = self._head.next
            prev_node = self._trail.prev

            # Connecting head and tail.
            self._head.next = self._trail
            self._trail.prev = self._head

            # Deprecating nodes chain in between head and tail
            # and setting size to 0.
            next_node.prev = prev_node.next = None
            self._size = 0

    def extend(self, iterable):
        """
        Adds the elements of a iterable to end of the Doubly Linked List.

        Args:
            iterable: takes an iterable object.
        """
        for element in iterable:
            self.append(element)

    def index(self, element):
        """
        Returns the index of element in Doubly Linked List and Raise exception
        if the given element not found on Doubly Linked List.

        Args:
            element: takes an object.

        Returns: an integer as index.
        """
        # Iterating over doubly linked list and searching given element.
        cursor = self._head.next
        index = 0
        while cursor != self._trail:
            # Securing type conflict while comparison
            if isinstance(cursor.data, type(element)) and cursor.data == element:
                break
            cursor = cursor.next
            index += 1

        # If the element not found we raise ValueError.
        if index >= self._size:
            raise ValueError(f'{element!r} not in list')
        else:
            return index

    def insert(self, index, element):
        """
        Inserts the given element at given index in Doubly Linked List.

        Args:
            index: takes an integer as index.
            element: takes an object.
        """
        # Filtering out negative values.
        if index < 0:
            NotImplementedError('Negative indexing not implemented yet')

        # Handling upper boundary case.
        if index > self._size:
            index = self._size

        # We're filtered the upper and lower boundaries
        # So that we can find nodes by counting.

        # Finding predecessor_node.
        predecessor_node = self._head
        for _ in range(index):
            predecessor_node = predecessor_node.next

        # Successor_node is placed after predecessor node.
        successor_node = predecessor_node.next

        # Performing insertion.
        self._insert_between(element, predecessor_node, successor_node)

    def is_empty(self):
        """
        Returns True if Doubly Linked List is empty else False.

        Returns: True if Doubly Linked List is empty else False.
        """
        return self._size == 0

    def pop(self, index=None):
        """
        Delete the given index in Doubly Linked List and returns the value in that index.
        If the index not present in the Doubly Linked List then raises IndexError.

        Args:
            index: takes an integer as index.

        Returns: deleted element in the list.
        """
        # Handling case empty list.
        if self.is_empty():
            raise IndexError('list is empty')

        # Handling default case None.
        if index is None:
            index = self._size - 1

        # Validating index.
        self._validate_index(index)

        # Walking through list and finding the node of given index.
        node = self._head.next
        for _ in range(index):
            node = node.next

        # Deleting node and returning the element.
        return self._delete_node(node)

    def remove(self, element):
        """
        Deletes the element if it is inside list else raise ValueError.

        Args:
            element: takes an object.
        """
        # Walking through the list and checking for matching
        node = self._head.next
        while node != self._trail:
            # Securing type conflict while comparison
            if isinstance(node.data, type(element)) and node.data == element:
                break
            node = node.next

        # Checking for ValueError and deleting node
        if node == self._trail:
            raise ValueError(f'{element!r} not in list')
        else:
            self._delete_node(node)

    def reverse(self):
        """
        Reverses the Doubly Linked List.
        """
        # For reversing, atleast 2 element needed inside the list.
        if self._size:
            # Taking previous node as header node and current node as
            # header node's next node.
            curr_node = self._head.next
            prev_node = self._head

            # Started flipping nodes previous and next along before trail node.
            while curr_node != self._trail:
                # Marking next node of current node
                next_node = curr_node.next

                # Flipping next and previous reference
                curr_node.prev = curr_node.next
                curr_node.next = prev_node

                # Moving prev_node and curr_node to next
                prev_node = curr_node
                curr_node = next_node

            # On before we're done flipping on nodes only between header and trail node.
            # So we need to connect them properly with header and trail nodes.

            # Taking previous node of trail as first node and next node of header as
            # last node.
            first_node = self._trail.prev
            last_node = self._head.next

            # Connecting header and first node with each other.
            self._head.next = first_node
            first_node.prev = self._head

            # Connecting trail and last node with each other.
            self._trail.prev = last_node
            last_node.next = self._trail


# --------------------------------------DRIVER-CODE-------------------------------------- #
if __name__ == '__main__':
    print('Running Tests,')

    # Creating list.
    print('\nCreating Linked List with range of 2,')
    dll = DoublyLinkedList(range(2))
    print(dll)

    # Appending some elements.
    print('\nAppending some elements,')
    dll.append(2.0)
    dll.append('string')
    print(dll)

    # Getting index.
    print("\nGetting index of 2.0 and 'string',")
    print(f'Value 2.0 is at index {dll.index(2.0)}')
    print(f"Value 'string' is at index {dll.index('string')}")

    # Inserting values.
    print('\nInserting values at index 1 and 5,')
    dll.insert(1, True)
    dll.insert(5, False)
    print(dll)

    # Changing some values.
    print('\nChanging values of index 0 and 3,')
    dll[0] = 99
    dll[3] = 109
    print(dll)

    # Reversing list.
    print('\nReversing list,')
    dll.reverse()
    print(dll)

    # Removing elements.
    print('\nRemoving elements False and 109,')
    dll.remove(False)
    dll.remove(109)
    print(dll)

    # Removing elements by index,
    print('\nRemoving elements at index 2 and 3,')
    dll.pop(3)
    dll.pop(2)
    print(dll)

    # Checking for empty and length.
    print('\nChecking for empty,')
    print(f'Empty: {dll.is_empty()}, Size: {len(dll)}')

    # Clearing list.
    print('\nClearing list,')
    dll.clear()
    print(dll)
    print(f'Empty: {dll.is_empty()}, Size: {len(dll)}')


# ----------------------------------------EXAMPLE---------------------------------------- #
'''
>>> from doubly_linked_list import *
>>> dll = DoublyLinkedList([1, 2, 3, 2.0, 3.0, 'alpha', ['a list']])
>>> dll
DoublyLinkedList([1, 2, 3, 2.0, 3.0, 'alpha', ['a list']])
>>> print(dll)
DoublyLinkedList: HEAD <=> 1 <=> 2 <=> 3 <=> 2.0 <=> 3.0 <=> 'alpha' <=> ['a list'] <=> END
>>> dll.pop()
['a list']
>>> dll.remove(2.0)
>>> dll
DoublyLinkedList([1, 2, 3, 3.0, 'alpha'])
>>> dll.append(99)
>>> dll
DoublyLinkedList([1, 2, 3, 3.0, 'alpha', 99])
>>> dll.extend(range(11, 15))
>>> dll
DoublyLinkedList([1, 2, 3, 3.0, 'alpha', 99, 11, 12, 13, 14])
>>> dll.index(3)
2
>>> dll.index('alpha')
4
>>> dll.insert(0, 0)
>>> dll
DoublyLinkedList([0, 1, 2, 3, 3.0, 'alpha', 99, 11, 12, 13, 14])
>>> dll[1] = True
>>> dll
DoublyLinkedList([0, True, 2, 3, 3.0, 'alpha', 99, 11, 12, 13, 14])
>>> dll.reverse()
>>> dll
DoublyLinkedList([14, 13, 12, 11, 99, 'alpha', 3.0, 3, 2, True, 0])
>>> len(dll)
11
>>> dll.clear()
>>> dll
DoublyLinkedList([])
>>> len(dll)
0

Complexity:
    +--------------+-----------------+
    |  Operations  | Time Complexity |
    +--------------+-----------------+
    |   append()   |       O(1)      |
    |   clear()    |       O(1)      |
    |   extend()   |     O(N + K)    |
    |   index()    |       O(N)      |
    |   insert()   |       O(N)      |
    |  is_empty()  |       O(1)      |
    |    pop()     |       O(N)      |
    |   remove()   |       O(N)      |
    |  reverse()   |       O(N)      |
    |    len()     |       O(1)      |
    | subscription |       O(N)      |
    +--------------+-----------------+
'''
