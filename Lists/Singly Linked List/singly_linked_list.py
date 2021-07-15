'''
Linked List:
    - Linked List is a linear data structure.
    - It contains collection of nodes that are connected through
      their references.
    - In this elements are not stored in contigious location.
    - This provides insertion and deletion in O(1) time.
    - It gives dynamic size allocation.

Singly Linked List:
    Singly Linked List is a type of Linked List in which every nodes
point the next node and last node points to null/None.

Aim:
    To implement the singly linked list in Python.

:URL: https://github.com/prathimacode-hub/PyAlgo-Tree/tree/main/Lists/singly_linked_list.py
:Author: NanthaKumar <nknanthakumar13@gmail.com>
:Contact: https://github.com/nknantha
:Date: 2021-07-15
'''


class SinglyLinkedList:
    '''
    Singly Linked List class.

    Attributes:
        head: Points the header node.
    '''

    __slots__ = '_head', '_length'

    class _Node:
        '''
        A simple class represents node.

        Attributes:
            data: The data which was given.
            next: Points the next node.
        '''

        __slots__ = 'data', 'next'

        def __init__(self, data=None, next=None):
            '''
            Creates Node instance.

            :param data: Stores the given value. (Default: None)
            :param next: Points the next node. (Default: None)
            '''
            self.data = data
            self.next = next

        def __str__(self):
            '''
            String representation of Node.

            :return: string representation of data stored in node.
            '''
            return str(self.data)

    def __init__(self, iterable=()):
        '''
        Creates Singly Linked List instance.

        :param iterable: takes iterable object if no argument is given empty Singly Linked List.
        '''
        # Initializing Header node
        self._head = self._Node('HEAD')
        # For storing length
        self._length = 0
        # For creating linked list using initial iterable
        self.extend(iterable)

    def __iter__(self):
        '''
        Returns iterator of Singly Linked List.

        :return: iterator of Singly Linked List.
        '''
        # Walking through list while yielding elements.
        curr = self._head.next
        while curr:
            yield curr.data
            curr = curr.next

    def __len__(self):
        '''
        Returns length of Singly Linked List.

        :return: length of Singly Linked List.
        '''
        return self._length

    def __repr__(self):
        '''
        Returns representation of Singly Linked list.

        :return: representation of Singly Linked list.
        '''
        # Here repr used for exactly represent what the data type looks like.
        return f"SinglyLinkedList([{', '.join(repr(el) for el in self.__iter__())}])"

    def __str__(self):
        '''
        Returns string version of Singly Linked List.

        :return: string version of Singly Linked List.
        '''
        # Here repr used for exactly represent what the data type looks like.

        # We can divide the string structure in to 3 parts.
        # 1) Prefix Part: 'SinglyLinkedList: HEAD -> '.
        # 2) Objects Part: Iteratively adding objects as string.
        # 3) Suffix Part: '-> END' used when list has elements.
        #                  and 'END' used when list has no elements.
        return 'SinglyLinkedList: HEAD -> ' \
            + ' -> '.join(repr(el) for el in self.__iter__()) \
            + ' -> ' * bool(self._length) + 'END'


    def __getitem__(self, index):
        '''
        Returns the object stored in the index.

        :param index: takes an integer as index.
        :return: the object stored in index.
        '''
        self.__validate_index(index)
        curr = self._head
        # Marking the HEAD node as -1 so that it not conflict with index access
        count = -1

        # Walking through the list and stops at given index
        while curr.next and count < index:
            curr = curr.next
            count += 1

        return curr.data

    def __setitem__(self, index, data):
        '''
        Assigns the given object at given index.

        :param index: takes an integer as index.
        :param data: the object to be stored in index.
        '''
        self.__validate_index(index)
        curr = self._head
        # Marking the HEAD node as -1 so that it not conflict with index access
        count = -1

        # Walking through the list and stops at given index
        while curr.next and count != index:
            curr = curr.next
            count += 1
        curr.data = data

    def __validate_index(self, index):
        '''
        Validates the index and raise Exceptions.

        :param index: takes an integer as index.
        '''
        # Checking for negative index
        if index < 0:
            raise NotImplementedError('Negative indexing not implemented yet')
        
        # Checking for index boundary
        if index >= self._length:
            raise IndexError('list index out of range')

    def append(self, data):
        '''
        Adds given object at the end of the Singly Linked List.

        :param data: takes an object.
        '''
        # Walking throught the last node
        curr = self._head
        while curr.next:
            curr = curr.next

        # Creating the node and append it in the list
        curr.next = self._Node(data)
        self._length += 1  # Increasing the length

    def clear(self):
        '''
        Clears the Singly Linked List.
        '''
        # Simply we change the HEAD's next to None
        self._head.next = None

        # And assings the length to 0
        self._length = 0

    def extend(self, iterable):
        '''
        Adds the elements of iterable in Singly Linked List.

        :param iterable: takes an iterable.
        '''
        # Walking through the list and finds last node
        curr = self._head
        while curr.next:
            curr = curr.next

        # From the end we start appending elements
        for element in iterable:
            curr.next = self._Node(element)
            self._length += 1
            curr = curr.next

    def index(self, data):
        '''
        Returns the index of the object data in Singly Linked List.

        :param data: takes an object.
        :return: index of the given object in Singly Linked List.
        '''
        # Walking through the list and finds element of given index
        curr = self._head.next
        index = 0
        while curr:
            # Here type() is used to diffrenciate multiple objects in python.
            if type(curr.data) == type(data) and curr.data == data:
                break
            curr = curr.next
            index += 1

        # If iteration reaches end we need to raise the ValueError
        if index >= self._length:
            raise ValueError(f'{data!r} not in list')
        else:
            return index

    def insert(self, index, data):
        '''
        Add the given object at given index.

        :param index: takes integer as index.
        :param data: takes an object.
        '''
        # Filtering negative index
        if index < 0:
            raise NotImplementedError('Negative indexing not implemented yet')

        # If index greater than our list's length, we simply
        # make an append operation.
        if index > self._length:
            index = self._length

        # Walking to the given index
        curr = self._head
        count = -1  # Marking the 'HEAD' node as -1
        while curr.next and count < index - 1:
            curr = curr.next
            count += 1

        # Creating and Inserting the new Node.
        new_node = self._Node(data)
        new_node.next = curr.next
        curr.next = new_node
        self._length += 1

    def is_empty(self):
        '''
        Returns True when Singly Linked List is Empty else False.

        :return: True when Singly Linked List is Empty else False.
        '''
        return self._length == 0

    def pop(self, index=None):
        '''
        Deletes the given index and returns the value. If index is None, deletes
        and returns the last index.

        :param index: takes integer as index. (Default: None)
        :return: deleted object in the list.
        '''
        # Checking for empty list
        if self.is_empty():
            raise IndexError('pop from empty list')

        # If index None then we need to delete the last index
        if index is None:
            index = self._length - 1

        self.__validate_index(index)

        # Walking to that index
        curr = self._head
        count = -1
        while curr.next and count < index - 1:
            curr = curr.next
            count += 1

        # Unlinking Operation
        data = curr.next.data
        curr.next = curr.next.next
        self._length -= 1
        return data

    def remove(self, data):
        '''
        Removes given object in Singly Linked List.

        :param data: takes an object.
        '''
        # Walking through the list and finding the object
        curr = self._head
        while curr.next:
            # Here type() is used to diffrenciate multiple objects in python.
            if type(curr.next.data) == type(data) and curr.next.data == data:
                break
            curr = curr.next
        
        # If object was not present we raise ValueError else we remove/unlink the node
        if curr.next is None:
            raise ValueError(f'{data!r} not in list')
        else:
            curr.next = curr.next.next
            self._length -= 1

    def reverse(self):
        '''
        Reverse the Singly Linked List in place.
        '''
        # Initially we store None in prev and the HEAD's after node in curr
        prev = None
        curr = self._head.next

        while curr:
            next_node = curr.next  # Marking the next node of current as next_node
            curr.next = prev  # Changing the link to the previous node
            prev = curr  # Marking the current node as previous
            curr = next_node  # Taking the next node from next_node

        self._head.next = prev  # Finally connecting the last node to the HEAD.


# --------------------------------------DRIVER-CODE------------------------------------------- #
if __name__ == '__main__':
    print('Creating Linked List with range of 5,')
    s = SinglyLinkedList(range(5))
    print(s)
    print('\nPrinting Individual Elements:')
    for el in s:
        print(el)
    print('\nChanging value of index 1,')
    s[1] = 99
    print(s)
    print(f'\nPopping {s.pop()},')
    print(s)
    print('\nClearing the list,')
    s.clear()
    print(s)


# -----------------------------------------EXAMPLE-------------------------------------------- #

'''
>>> from singly_linked_list import *
>>> s = SinglyLinkedList()
>>> s
SinglyLinkedList([])
>>> s.append(1)
>>> s
SinglyLinkedList([1])
>>> s.extend([4, 5, 6, 7])
>>> s
SinglyLinkedList([1, 4, 5, 6, 7])
>>> s[0]
1
>>> s[0] = 99
>>> s
SinglyLinkedList([99, 4, 5, 6, 7])
>>> s.insert(1, 100)
>>> s
SinglyLinkedList([99, 100, 4, 5, 6, 7])
>>> s.pop()
7
>>> s
SinglyLinkedList([99, 100, 4, 5, 6])
>>> s.remove(6)
>>> s
SinglyLinkedList([99, 100, 4, 5])
>>> s.clear()
>>> s
SinglyLinkedList([])

COMPLEXITY:
    +-----------+-----------------+
    |  Methods  | Time Complexity |
    |-----------+-----------------+
    | append()  |      O(N)       |
    | clear()   |      O(1)       |
    | extend()  |    O(N + K)     |
    | index()   |      O(K)       |
    | insert()  |      O(K)       |
    |  pop()    |      O(K)       |
    | remove()  |      O(K)       |
    | reverse() |      O(N)       |
    +-----------+-----------------+
'''
