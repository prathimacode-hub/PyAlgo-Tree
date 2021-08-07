class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class CircularLinkedList(object):

    def __init__(self, head=None, end=None):
        '''
            Initalize a linke list with a head and a tail.
        '''

        self.head = head
        self.end = end

    def traverse(self):
        '''
            Traverse the list and print each value.
            Time Complexity: O(n)
        '''

        # define the first node
        curr_node = self.head

        # as long as there is a next node, keep going
        while curr_node.next_node:

            # print the data
            print(curr_node.data)

            # reassign the next node
            curr_node = curr_node.next_node

            # here is the issue, if we don't add this condition we get an infinite loop.
            # Once the current node is the head again, then exit the loop.
            if curr_node == self.head:
                break

    def insert_end(self, data):
        '''
            Insert a node at the end of our linked list.
            Time Complexity: O(1)
        '''

        new_node = Node(data)

        # handle empty list case
        if self.head == None:
            self.head = new_node
            self.head.next_node = new_node
            self.end = new_node
            return

        # handle non-empty list case
        if self.end != None:
            self.end.next_node = new_node
            new_node.next_node = self.head
            self.end = new_node
            return

    def insert_beg(self, data):
        '''
            Insert a node at the beginning of our linked list.
            Time Complexity: O(1)
        '''

        new_node = Node(data)
        new_node.next_node = self.head
        curr_node = self.head

        # handle empty list case
        if curr_node == None:
            self.head = new_node
            self.end = new_node
            self.head.next_node = new_node
            return

        # handle non-empty list case
        if self.end != None:
            self.end.next_node = new_node
            new_node.next_node = self.head
            self.head = new_node
            return

    def insert_mid(self, ref_node, data):
        '''
            Insert a node at the middle of our linked list, after a given node.
            Time Complexity: O(1)
        '''

        # handle empty node case
        if ref_node == None:
            print("You've selected an empty node.")

        # if we are inserting after the end node, then just use the insert_end method
        if ref_node == self.end:
            self.insert_end(data)
            return

        # otherwise it's a true mid.
        new_node = Node(data)
        ref_next = ref_node.next_node
        ref_node.next_node = new_node
        new_node.next_node = ref_next

    def delete_beg(self):
        '''
            Delete a node at the beginning of our list.
            Time Complexity: O(1)
        '''

        if self.head != None:

            # grab the node that comes after the head.
            aft_head = self.head.next_node

            # have the last node now point to that node
            self.end.next_node = aft_head

            # set the head property.
            self.head = aft_head

        else:
            raise ValueError("The list is empty")

    def delete_end(self):
        '''
            Delete a node at the end of our list.
            Time Complexity: O(1)
        '''

        if self.end != None:

            # grab the head
            curr_node = self.head

            # traverse until the end
            while curr_node.next_node.next_node != self.head:
                curr_node = curr_node.next_node

            # set the last node equal to the node before the last one.
            self.end = curr_node

            # have the new last node link to the head.
            curr_node.next_node = self.head

        else:
            raise ValueError("The list is empty")

    def delete_mid(self, position):
        '''
            Delete a node in the middle of our list, after that given node.
            Time Complexity: O(n)
        '''

        # if position is 0 then delete first.
        if position == 0:
            self.delete_beg()
            return

        # if position is the size of the list then delete the last one.
        if position == self.list_size():
            self.delete_end()
            return

        # grab the node after the head.
        curr_node = self.head.next_node

        # initalize count
        count = 0

        # traverse till you reach the position
        while count <= position:
            count = count + 1
            curr_node = curr_node.next_node

        # have it point to the node after the one you want to delete.
        curr_node.next_node = curr_node.next_node.next_node

    def list_size(self):
        '''
            Return the size of our list.
            Time Complexity: O(n)
        '''

        # grab the head
        curr_node = self.head
        count = 0

        # traver until you reach the head again
        while curr_node.next_node:

            count = count + 1
            curr_node = curr_node.next_node

            # prevents infinite loop
            if curr_node == self.head:
                break

        return count

    def get_prev_node(self, ref_node):
        '''
            Return the node before a given reference node.
            Time Complexity: O(n)
        '''

        # handle empty list case
        if self.head is None:
            raise ValueError("The list is empty")

        # define the first node
        current = self.head

        # keep going until you reach the desired node.
        while current.next_node != ref_node:
            current = current.next_node

        return current

    def reverse(self):
        '''
            Reverse the circular list, so that the tail is now the head.
            Time Complexity: O(n)
        '''

        # if the head is empty return
        if self.head is None:
            raise ValueError("The list is empty")

        # initalize a few of our variables
        last = self.head
        curr = self.head
        prev = self.end
        next = curr.next_node

        # reassign the last node to the head's next node
        curr.next_node = prev

        # the old previous now becomes the old current
        prev = curr

        # the old current now becomes the old next, the one after the head
        curr = next

        # keep going until you reach the last node
        while curr != last:
            # reassign next
            next = curr.next_node

            # do the same reassignment steps as upabove
            curr.next_node = prev
            prev = curr
            curr = next

        # one final reassignment, make sure the last node points to the head
        curr.next_node = prev

        # then redefine your head and tail.
        self.head = prev
        self.end = curr

    def split_list(self, head1, head2):
        '''
            Split the list into two separate circular linked list.
            Time Complexity: O(n)

            PARA: head1
            TYPE: CircularLinkedList

            PARA: head2
            TYPE: CircularLinkedList
        '''

        slow_ptr = self.head
        fast_ptr = self.head

        # handle empty list case
        if self.head is None:
            raise ValueError("The list is empty")

        # For ODD NODES: fast_ptr.next_node will become the head.
        # For EVEN NODES: fast_ptr.next_node.next_node will become the head.
        while (fast_ptr.next_node != self.head and fast_ptr.next_node.next_node != self.head):
            fast_ptr = fast_ptr.next_node.next_node
            slow_ptr = slow_ptr.next_node

        # if the fast pointer next next is the head, just stop one node before to get the last element of our list.
        if fast_ptr.next_node.next_node == self.head:
            fast_ptr = fast_ptr.next_node

        # Set the head pointer of first half
        head1.head = self.head

        # Set the head pointer of second half
        if self.head.next_node != self.head:
            head2.head = slow_ptr.next_node

        # Make second half circular
        fast_ptr.next_node = slow_ptr.next_node

        # Make first half circular
        slow_ptr.next_node = self.head

    def split_list_2(self, head1, head2):
        '''
            Split the list into two separate circular linked list.
            Time Complexity: O(n)

            PARA: head1
            TYPE: CircularLinkedList

            PARA: head2
            TYPE: CircularLinkedList
        '''

        # grab the list size
        list_size = self.list_size()

        # grab the midpoint
        mid = list_size // 2

        # get the first node
        curr = self.head

        # go while the count is less than the list size
        count = 0
        while count <= list_size - 1:

            # grab the data
            data = curr.data

            # if it's less than the mid, put in list one
            if count < mid:
                head1.insert_beg(data)

            # if it's greater than the mid, put it in list two
            if count >= mid:
                head2.insert_beg(data)

            # grab the next node.
            curr = curr.next_node

            # increment the counter
            count = count + 1


# define a new list
circular_list = CircularLinkedList()

# insert a few values at the end
circular_list.insert_end(50)
circular_list.insert_end(60)
circular_list.insert_end(70)

# insert a few values at the beginning
circular_list.insert_beg(90)
circular_list.insert_beg(100)

print('After Insertion')
print('-' * 20)
circular_list.traverse()

# grab a node
first_node = circular_list.end

# insert value inbetween two nodes.
circular_list.insert_mid(first_node, 20)

print('After Mid Insertion')
print('-' * 20)
circular_list.traverse()

# delete the first and last value
circular_list.delete_beg()
circular_list.delete_end()

print('Before Reversal, and after deletion')
print('-' * 20)
circular_list.traverse()

# reverse the list
circular_list.reverse()

print('After Reversal')
print('-' * 20)
circular_list.traverse()

# return the list size
circular_list.list_size()

# delete a node at position 3
circular_list.delete_mid(3)

print('After Mid Deletion')
print('-' * 20)
circular_list.traverse()

# grab the node before the second node
second_node = circular_list.head.next_node
circular_list.get_prev_node(second_node)

# define two new lists
head1 = CircularLinkedList()
head2 = CircularLinkedList()

circular_list.split_list_2(head1, head2)
# # split the lists
# circular_list.split_list(head1, head2)


print('List One')
print('-' * 20)
head1.traverse()

print('List Two')
print('-' * 20)
head2.traverse()
