'''
- A linked list is similar to an array, it holds values. However, links in a linked list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer,
together with next pointer and data which are there in singly linked list.
 - Advantages over SLL - IT can be traversed in both forward and backward direction.,Delete operation is more efficent'''
from __future__ import print_function


class Node:
    next = None  # This points to the link in front of the new node
    previous = None  # This points to the link behind the new node

    def __init__(self, data):
        self.value = data

    def display(self):
        print("{}  <-> ".format(self.value), end=" ")


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_head(self, data):
        new_node = Node(data)                            # Create a new node with a value attached to it
        if self.is_empty():                            # Set the first element added to be the tail
            self.tail = new_node
        else:
            self.head.previous = new_node             # new_node <-- currenthead(head)
        new_node.next = self.head                     # new_node <--> currenthead(head)
        self.head = new_node                          # new_node(head) <--> oldhead

    def insert_tail(self, data):
        new_node = Node(data)
        new_node.next = None                         # currentTail(tail)    new_node -->
        self.tail.next = new_node                    # currentTail(tail) --> new_node -->
        new_node.previous = self.tail                #currentTail(tail) <--> new_node -->
        self.tail = new_node                         # oldTail <--> new_node(tail) -->
    
    def delete_head(self):
        temp = self.head
        self.head = self.head.next                   # oldHead <--> 2ndElement(head)
        self.head.previous = None                    # oldHead --> 2ndElement(head) nothing pointing at it so the old head will be removed
        if self.head is None:
            self.tail = None                         # if empty linked list
        return temp
    
    def delete_tail(self):
        temp = self.tail
        self.tail = self.tail.previous              # 2ndLast(tail) <--> oldTail --> None
        self.tail.next = None                       # 2ndlast(tail) --> None
        return temp
    
    def delete_item(self, data):
        current = self.head
        while current.value != data and current.next:                  # Find the position to delete
            current = current.next
            
        if current == self.head:
            self.delete_head()
        elif current == self.tail:
            self.delete_tail()
        else:                                           # Before: 1 <--> 2(current) <--> 3
            current.previous.next = current.next        # 1 --> 3
            current.next.previous = current.previous    # 1 <--> 3

    def get(self, data):
        """
        Method finds and returns item and its position started from the head.
        """
        if not self.head:
            return None, None

        current = self.head
        position = 0
        while current.value != data and current.next:
            current = current.next
            position += 1
        if current.value == data:
            return current, position
        return None, None

    def is_empty(self):
        return self.head is None
        
    def display(self):                                # Prints contents of the list
        current = self.head
        while current:
            current.display()
            current = current.next  
        print('[end of list]')


if __name__ == '__main__':
    import random
    # insert 5 elements from the head
    random_list = random.sample(range(0, 10), 5)
    random.shuffle(random_list)
    print('\nAdding', random_list, 'list from the head.')
    linked_list = LinkedList()
    for i in random_list:
        linked_list.insert_head(i)
    linked_list.display()

    # insert 5 elements from the tail
    random_list = random.sample(range(50, 100), 5)
    random.shuffle(random_list)
    print('\nAdding', random_list, 'list from the tail.')
    for i in random_list:
        linked_list.insert_tail(i)
    linked_list.display()

    print('\nFinding', random_list[0], 'element.')
    node, position = linked_list.get(random_list[0])
    if node:
        print('Found {} at {} position from the head.'.
              format(node.value, position))

    print('\nDeleting 3 elements from the head.')
    for _ in range(3):
        linked_list.delete_head()
    linked_list.display()

    print('\nDeleting 3 elements from the tail.')
    for _ in range(3):
        linked_list.delete_tail()
    linked_list.display()

