class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, node):
        self.head = Node(node, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            node = self.head.item
            self.head = self.head.next
            return node

    def is_empty(self):
        return self.head is None

    def traverse(self):
        """ docstring for function """
        node = self.head
        while node:
            print(node.item, " => ", end='')
            node = node.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.add(4)
    ll.add(0)
    ll.add(3)
    ll.add(6)
    print(ll.traverse())
    ll.remove()
    print(ll.traverse())
