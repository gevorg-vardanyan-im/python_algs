from __future__ import print_function


class Node:  # create a Node
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.Head = None

    def insert_tail(self, data):
        if not self.Head:
            self.insert_head(data)
        else:
            temp = self.Head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def insert_head(self, data):
        new_node = Node(data)
        if self.Head is not None:
            new_node.next = self.Head
        self.Head = new_node

    def print_list(self):
        temp = self.Head
        while temp:
            print(temp.data, '-->', end=' ')
            temp = temp.next
        print('[end of list]')

    def delete_head(self):
        temp = self.Head
        if self.Head:
            self.Head = self.Head.next
            temp.next = None
        return temp

    def delete_tail(self):
        temp = self.Head
        if self.Head:
            if not self.Head.next:
                self.Head = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next, temp = None, temp.next
        return temp

    def is_empty(self):
        return self.Head is None

    def reverse(self):
        prev = None
        current = self.Head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.Head = prev


def main():
    import random
    # insert 5 elements from the head
    random_list = random.sample(range(0, 10), 5)
    random.shuffle(random_list)
    print('\nAdding', random_list, 'list from the head.')
    linked_list = LinkedList()
    for i in random_list:
        linked_list.insert_head(i)
    linked_list.print_list()

    # insert 5 elements from the tail
    random_list = random.sample(range(50, 100), 5)
    random.shuffle(random_list)
    print('\nAdding', random_list, 'list from the tail.')
    for i in random_list:
        linked_list.insert_tail(i)
    linked_list.print_list()

    print('\nReversing the list.')
    linked_list.reverse()
    linked_list.print_list()

    print('\nDeleting 3 elements from the head.')
    for _ in range(3):
        linked_list.delete_head()
    linked_list.print_list()

    print('\nDeleting 3 elements from the tail.')
    for _ in range(3):
        linked_list.delete_tail()
    linked_list.print_list()
    # print("\nDelete Head")
    # A.delete_head()
    # print("Delete Tail")
    # A.delete_tail()
    # print("\nPrint List : ")
    # A.print_list()
    # print("\nReverse Linked List")
    # A.reverse()
    # print("\nPrint List : ")
    # A.print_list()


if __name__ == '__main__':
    main()
