'''
====================
 Singly Linked List
====================
:Description: A Python implementation of singly linked list using nodes.
:URL: https://github.com/prathimacode-hub/PyAlgo-Tree/tree/main/Lists/singly_linked_list.py
:Author: NanthaKumar <nknanthakumar13@gmail.com>
:Date: 2021-07-12
:Contact: https://www.linkedin.com/in/nanthakumar13/
'''


class Node:
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


class SinglyLinkedList:
    '''
    Singly Linked List class.

    Attributes:
        head: Points the header node.
    '''

    __slots__ = 'head', '_length'

    def __init__(self, iterable=()):
        '''
        Creates Singly Linked List instance.

        :param iterable: takes iterable object if no argument is given empty Singly Linked List.
        '''
        # Initializing Header node
        self.head = Node('HEAD')
        # For storing length
        self._length = 0

        self.extend(iterable)

    def __iter__(self):
        '''
        Returns iterator of Singly Linked List.

        :return: iterator of Singly Linked List.
        '''
        curr = self.head.next
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
        return f"SinglyLinkedList([{', '.join(repr(el) for el in self.__iter__())}])"

    def __str__(self):
        '''
        Returns string version of Singly Linked List.

        :return: string version of Singly Linked List.
        '''
        return 'SinglyLinkedList: HEAD -> ' + ' -> '.join(repr(el) for el in self.__iter__())

    def __getitem__(self, index):
        '''
        Returns the value stored in the index.

        :param index: takes an integer as index.
        :return: the value stored in index.
        '''
        self.__validate_index(index)
        curr = self.head
        count = -1
        while curr.next and count < index:
            curr = curr.next
            count += 1

        return curr.data

    def __setitem__(self, index, object):
        '''
        Assigns the given value at given index.

        :param index: takes an integer as index.
        :param object: the to be stored in index.
        '''
        self.__validate_index(index)
        curr = self.head
        count = -1
        while curr.next and count != index:
            curr = curr.next
            count += 1
        curr.data = object

    def __validate_index(self, index):
        '''
        Validates the index and raise Exceptions.

        :param index: takes an integer as index.
        '''
        if index < 0:
            raise NotImplementedError('Negative indexing not implemented yet')
        if index >= self._length:
            raise IndexError('list index out of range')

    def append(self, object):
        '''
        Adds given object at the end of the Singly Linked List.

        :param object: takes an object.
        '''
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = Node(object)
        self._length += 1

    def extend(self, iterable):
        '''
        Adds the elements of iterable in Singly Linked List.

        :param iterable: takes an iterable.
        '''
        curr = self.head
        while curr.next:
            curr = curr.next

        for element in iterable:
            curr.next = Node(element)
            self._length += 1
            curr = curr.next

    def insert(self, index, object):
        '''
        Add the given object at given index.

        :param index: takes integer as index.
        :param object: takes an object.
        '''
        # Filtering negative index
        if index < 0:
            raise NotImplementedError('Negative indexing not implemented yet')

        # If index greater than our list's length, we simply
        # make an append operation.
        if index > self._length:
            index = self._length

        curr = self.head
        count = -1  # Marking the 'HEAD' node as -1
        while curr.next and count < index - 1:
            curr = curr.next
            count += 1

        new_node = Node(object)
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
        if self.is_empty():
            raise IndexError('pop from empty list')

        if index is None:
            index = self._length - 1

        self.__validate_index(index)
        curr = self.head
        count = -1
        while curr.next and count < index - 1:
            curr = curr.next
            count += 1

        object = curr.next.data
        curr.next = curr.next.next
        self._length -= 1
        return object

    def reverse(self):
        '''
        Reverse the Singly Linked List in place.
        '''
        prev = None
        curr = self.head.next

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head.next = prev

    def clear(self):
        '''
        Clears the Singly Linked List.
        '''
        self.head.next = None
        self._length = 0

    def index(self, object):
        '''
        Returns the index of the given object in Singly Linked List.

        :param object: takes an object.
        :return: index of the given object in Singly Linked List.
        '''
        curr = self.head.next
        index = 0
        while curr and curr.data != object:
            curr = curr.next
            index += 1

        if index >= self._length:
            raise ValueError(f'{object!r} not in list')
        else:
            return index

    def remove(self, object):
        '''
        Removes given object in Singly Linked List.

        :param object: takes an object.
        '''
        curr = self.head
        while curr.next and curr.next.data != object:
            curr = curr.next

        if curr.next is None:
            raise ValueError(f'{object!r} not in list')
        else:
            curr.next = curr.next.next
            self._length -= 1


if __name__ == '__main__':
    print('Creating Linked List with range of 5,')
    s = SinglyLinkedList(range(5))
    print(s)
    print('Printing Individual Elements:')
    for el in s:
        print(el)
    print('Changing value of index 1,')
    s[1] = 99
    print(s)
    print(f'Popping {s.pop()},')
    print(s)
    print('Clearing the list,')
    s.clear()
    print(s)